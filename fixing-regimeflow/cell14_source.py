import os
import sys

# Ensure stdout/stderr use UTF-8 encoding (especially on Windows)
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
if hasattr(sys.stderr, 'reconfigure'):
    try:
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

import numpy as np
import pandas as pd
import torch
from typing import List, Dict, Tuple

# 1. Define the paper's regime categories & evaluation mappings
REGIME_GROUPS = {
    "Complex": [0],
    "Stable": [1, 2],
    "Oscillatory": [3],
    "Monotonic": [4, 5]
}

REGIME_NAMES = {
    0: "Complex (directly_stable)",
    1: "Stable (inc_stable)",
    2: "Stable (dec_stable)",
    3: "Oscillatory (oscillation)",
    4: "Monotonic (increasing)",
    5: "Monotonic (decreasing)"
}

# Mapping of model name/dir to display name and group for Table 1
DISPLAY_TO_MODEL = {
    "DLinear": ["DLinear"],
    "iTransformer": ["iTransformer"],
    "PatchTST": ["PatchTST"],
    "TimeMixer": ["TimeMixer"],
    "TimeXer": ["TimeXer"],
    "SMamba": ["S_Mamba", "SMamba"],
    "BiMamba4TS": ["BiMamba4TS"],
    "NSFormer": ["NSformer", "NSFormer"],
    "Chronos": ["Chronos"],
    "CSDI": ["CSDI"],
    "TSDiff": ["TSDiff"],
    "TSFlow": ["TSFlow_PE", "TSFlow"],
    "Ours": ["RegimeFlow_no_cond", "RegimeFlow_no_regime"],
    "CSDI†": ["CSDI_regime"],
    "TSDiff†": ["TSDiff_regime"],
    "TSFlow†": ["TSFlow_PE_regime"],
    "Ours†": ["RegimeFlow"]
}

MODEL_ORDER = [
    ("Point Forecasting", ["DLinear", "iTransformer", "PatchTST", "TimeMixer", "TimeXer", "SMamba", "BiMamba4TS", "NSFormer", "Chronos"]),
    ("Probabilistic Forecasting w/o Regime Condition", ["CSDI", "TSDiff", "TSFlow", "Ours"]),
    ("Probabilistic Forecasting w/ Regime Condition", ["CSDI†", "TSDiff†", "TSFlow†", "Ours†"])
]

def dataframe_to_markdown(df: pd.DataFrame) -> str:
    """
    Convert a pandas DataFrame to a markdown table string.
    Bypasses the need for the external 'tabulate' library.
    """
    if df.empty:
        return ""
    
    cols = list(df.columns)
    rows = df.values.tolist()
    
    # Calculate column widths
    widths = [len(str(c)) for c in cols]
    for row in rows:
        for i, val in enumerate(row):
            widths[i] = max(widths[i], len(str(val)))
            
    # Format header
    header = "| " + " | ".join(f"{str(cols[i]):<{widths[i]}}" for i in range(len(cols))) + " |"
    separator = "| " + " | ".join("-" * widths[i] for i in range(len(cols))) + " |"
    
    # Format rows
    formatted_rows = []
    for row in rows:
        formatted_rows.append("| " + " | ".join(f"{str(row[i]):<{widths[i]}}" for i in range(len(row))) + " |")
        
    return "\n".join([header, separator] + formatted_rows)

def get_display_name_and_group(model_name: str) -> Tuple[str, str]:
    for group, display_list in MODEL_ORDER:
        for disp in display_list:
            if model_name in DISPLAY_TO_MODEL[disp] or model_name.split('_seed')[0] in DISPLAY_TO_MODEL[disp]:
                return disp, group
    return model_name, "Other"

def parse_args() -> Dict:
    """Simple parser for key=value command line arguments."""
    args = {}
    for arg in sys.argv[1:]:
        if '=' in arg:
            k, v = arg.split('=', 1)
            k = k.strip()
            v = v.strip()
            # Clean boolean values
            if v.lower() == 'true':
                v = True
            elif v.lower() == 'false':
                v = False
            # Clean list values (e.g. condition_names=[a,b])
            elif v.startswith('[') and v.endswith(']'):
                v = [x.strip() for x in v[1:-1].split(',')]
            else:
                # Try to parse as int or float
                try:
                    if '.' in v:
                        v = float(v)
                    else:
                        v = int(v)
                except ValueError:
                    pass
            args[k] = v
    return args

def discover_npz_files(save_path_dir: str) -> Dict[str, Dict[int, str]]:
    """
    Scan save_path_dir recursively for test_predictions.npz.
    Returns: { model_name: { seed: npz_path } }
    """
    discovered = {}
    if not os.path.exists(save_path_dir):
        return discovered
        
    for root, dirs, files in os.walk(save_path_dir):
        for file in files:
            if file == 'test_predictions.npz':
                full_path = os.path.join(root, file)
                norm_path = os.path.normpath(full_path).replace('\\', '/')
                parts = norm_path.split('/')
                
                model_name = None
                seed = None
                
                # Try to extract model name and seed from path parts
                # e.g., results/predictions/RegimeFlow_seed53/53/test_predictions.npz
                # or results/checkpoints/RegimeFlow_seed53/test_predictions.npz
                for part in parts:
                    if '_seed' in part:
                        model_name = part.split('_seed')[0]
                        try:
                            seed_str = part.split('_seed')[1]
                            seed = int(''.join(filter(str.isdigit, seed_str)))
                        except Exception:
                            pass
                        break
                    elif part.startswith('full_') and part.endswith('_eval'):
                        model_name = part[5:-5]
                        break
                        
                if model_name is None and len(parts) >= 2:
                    model_name = parts[-2]
                
                # Check if there is a directory part that is a digit (representing seed)
                for part in parts:
                    if part.isdigit():
                        seed = int(part)
                        
                if model_name:
                    if seed is None:
                        seed = 53  # fallback
                    if model_name not in discovered:
                        discovered[model_name] = {}
                    discovered[model_name][seed] = full_path
                    
    return discovered

def load_dataset_and_patterns(
    seed: int,
    system_info_path: str,
    data_dir: str,
    is_ood: bool,
    input_window: int,
    output_window: int,
    stride: int,
    transform_type: str,
    condition_names: List[str]
) -> np.ndarray:
    """Helper to load and partition the test dataset for a specific seed."""
    system_info = pd.read_csv(system_info_path)
    all_files = [
        os.path.join(data_dir, 'Data', row['model_id'], row['model_name'] + '.csv')
        for _, row in system_info.iterrows()
    ]
    
    # Check if files exist
    existing_files = [f for f in all_files if os.path.exists(f)]
    if not existing_files:
        print(f"[-] Error: CSV trajectory files not found in: {os.path.join(data_dir, 'Data')}")
        return None
        
    if is_ood:
        from sklearn.model_selection import train_test_split
        _, test_list = train_test_split(
            all_files, test_size=0.2, random_state=seed
        )
        
        from dataset.BioSeries import MultiBioSeriesDataset
        test_ds = MultiBioSeriesDataset(
            dataset_dirs=test_list,
            input_window=input_window,
            output_window=output_window,
            stride=stride,
            variable_independent=True,
            transform_type=transform_type,
            condition_names=condition_names
        )
    else:
        from dataset.BioSeries import MultiBioSeriesDataset, MultiBioSeriesDataset_Subset
        from sklearn.model_selection import train_test_split
        
        all_dataset = MultiBioSeriesDataset(
            dataset_dirs=all_files,
            input_window=input_window,
            output_window=output_window,
            stride=stride,
            variable_independent=True,
            transform_type=transform_type,
            condition_names=condition_names
        )
        all_list = list(range(len(all_dataset)))
        _, test_indices = train_test_split(
            all_list, test_size=0.2, random_state=seed
        )
        test_ds = MultiBioSeriesDataset_Subset(all_dataset, test_indices)

    # Build lookup lists for True Regime IDs
    parent_ds = test_ds
    is_subset = False
    if hasattr(test_ds, 'dataset'):
        is_subset = True
        parent_ds = test_ds.dataset.dataset
        indices = test_ds.dataset.indices
    elif hasattr(test_ds, 'subset_indices') and test_ds.subset_indices is not None:
        is_subset = True
        parent_ds = test_ds
        indices = test_ds.subset_indices

    parent_patterns = []
    for base_ds in parent_ds.base_datasets:
        num_vars = base_ds.num_vars
        total_window = base_ds.input_window + base_ds.output_window
        max_start = base_ds.length - total_window
        num_windows = 0
        if max_start >= 0:
            num_windows = (max_start // base_ds.stride) + 1
            
        if num_windows == 0:
            continue
            
        traj_patterns = base_ds.system_condition['traj_pattern'][1:] # skip time column
        
        for var_idx in range(num_vars):
            pat = int(np.round(traj_patterns[var_idx]))
            parent_patterns.extend([pat] * num_windows)
            
    parent_patterns = np.array(parent_patterns)
    
    if is_subset:
        true_patterns = parent_patterns[indices]
    else:
        true_patterns = parent_patterns
        
    print(f"Total test dataset samples indexed for partition seed {seed}: {len(true_patterns)}")
    return true_patterns

def evaluate_model_suite(
    save_path_dir: str = "./results",
    experiment_base_name: str = None,  # if None, discovers/evaluates all
    seeds: List[int] = [42],
    data_dir: str = "./SysBio-Traj",
    load_name: str = "SysBio-Traj_index.csv",
    input_window: int = 96,
    output_window: int = 256,
    stride: int = 16,
    transform_type: str = "minmax",
    condition_names: List[str] = ["bound_min", "bound_max", "traj_pattern", "period"],
    is_ood: bool = True,
    partition_seed: int = 42,
    npz_path: str = None
):
    """
    Evaluate saved test_predictions.npz files across multiple seeds,
    aligning samples with dataset metadata to calculate stratified MSE and MAE.
    """
    print("=" * 70)
    print(f"Beginning Cross-Seed Stratified Evaluation")
    print(f"Data Dir: {data_dir}")
    print(f"Results Dir: {save_path_dir}")
    print("=" * 70)
    
    # 1. Add python path to help load local modules
    if '__file__' in globals():
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    else:
        project_root = os.path.abspath('.')
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
        
    # 2. Check if data directory exists
    system_info_path = os.path.join(data_dir, load_name)
    if not os.path.exists(system_info_path):
        print(f"[-] Error: Dataset index not found at: {system_info_path}")
        print("Please place the SysBio-Traj dataset in the workspace or run with data.data_dir=<path>")
        return None

    # Cache for true_patterns to avoid rebuilding repeatedly for the same partition seed
    patterns_cache = {}
    
    # 4. Resolve which models and files to evaluate
    model_prediction_files = {} # { model_name: { seed: npz_path } }
    
    if npz_path is not None:
        # Directly evaluate a single npz file
        model_name = experiment_base_name if experiment_base_name else "Custom"
        model_prediction_files[model_name] = {seeds[0]: npz_path}
    else:
        # Auto-discover or filter by experiment_base_name
        discovered = discover_npz_files(save_path_dir)
        if experiment_base_name:
            # Single or comma-separated list of models
            model_keys = [m.strip() for m in experiment_base_name.split(',')]
            if len(model_keys) == 1 and model_keys[0].lower() == 'all':
                model_prediction_files = discovered
            else:
                for k in model_keys:
                    if k in discovered:
                        model_prediction_files[k] = discovered[k]
                    else:
                        print(f"[-] Warning: No prediction files discovered for model: {k}")
        else:
            # Default: evaluate all discovered models
            model_prediction_files = discovered

    if not model_prediction_files:
        print("[-] No prediction files found for evaluation.")
        return None

    # 5. Evaluate each model
    all_model_results = {} # { display_name: { category: { mse_list, mae_list } } }

    for model_name, seed_paths in model_prediction_files.items():
        disp_name, group_name = get_display_name_and_group(model_name)
        print(f"\nEvaluating Model: {model_name} (Display: {disp_name})")
        
        seed_metrics = {group: {"mse": [], "mae": []} for group in list(REGIME_GROUPS.keys()) + ["Overall"]}
        
        # Determine which seeds to process for this model
        seeds_to_process = [s for s in seeds if s in seed_paths]
        if not seeds_to_process:
            raise ValueError(
                f"\n[CRITICAL ERROR] No prediction files found for the requested seed(s) {seeds} "
                f"for model '{model_name}'.\n"
                f"Available seeds for this model in results/predictions: {list(seed_paths.keys()) if seed_paths else 'None'}.\n"
                f"This indicates that the evaluation for seed {seeds} was either skipped or failed. "
                f"Please ensure you run evaluation for seed {seeds} first, and check eval_{model_name}.log for errors."
            )
            
        for seed in seeds_to_process:
            path = seed_paths.get(seed, None)
            if path is None:
                continue
                
            if not os.path.exists(path):
                continue
                
            print(f"  [+] Processing seed {seed} prediction from: {path}")
            
            # Load true patterns dynamically using the seed as the partition seed
            if seed not in patterns_cache:
                patterns_cache[seed] = load_dataset_and_patterns(
                    seed=seed,
                    system_info_path=system_info_path,
                    data_dir=data_dir,
                    is_ood=is_ood,
                    input_window=input_window,
                    output_window=output_window,
                    stride=stride,
                    transform_type=transform_type,
                    condition_names=condition_names
                )
                
            true_patterns = patterns_cache[seed]
            if true_patterns is None:
                print(f"  [-] Warning: Failed to load dataset patterns for seed {seed}. Skipping seed.")
                continue
                
            npz_data = np.load(path)
            preds = npz_data['predictions']
            targets = npz_data['targets']
            
            if preds.ndim == 3 and preds.shape[-1] == 1:
                preds = preds.squeeze(-1)
            if targets.ndim == 3 and targets.shape[-1] == 1:
                targets = targets.squeeze(-1)
                
            if len(preds) != len(true_patterns):
                print(f"  [-] WARNING: Predictions count ({len(preds)}) does not match dataset patterns count ({len(true_patterns)}) for seed {seed}.")
                print(f"      Attempting to search for matching partition seed based on predictions length...")
                matched = False
                for alt_seed in [42, 53, 25, 81]:
                    if alt_seed not in patterns_cache:
                        patterns_cache[alt_seed] = load_dataset_and_patterns(
                            seed=alt_seed,
                            system_info_path=system_info_path,
                            data_dir=data_dir,
                            is_ood=is_ood,
                            input_window=input_window,
                            output_window=output_window,
                            stride=stride,
                            transform_type=transform_type,
                            condition_names=condition_names
                        )
                    alt_patterns = patterns_cache[alt_seed]
                    if alt_patterns is not None and len(preds) == len(alt_patterns):
                        print(f"      [+] Found matching partition seed: seed {alt_seed} (length {len(alt_patterns)}). Re-aligning!")
                        true_patterns = alt_patterns
                        matched = True
                        break
                if not matched:
                    print(f"      [-] Could not find any seed split matching prediction length of {len(preds)}.")
                    print(f"      Metrics for each regime category will be completely scrambled!")
                
            min_size = min(len(preds), len(true_patterns))
            preds = preds[:min_size]
            targets = targets[:min_size]
            aligned_patterns = true_patterns[:min_size]
            
            # Group-wise metrics
            for group_cat, p_ids in REGIME_GROUPS.items():
                mask = np.isin(aligned_patterns, p_ids)
                if np.sum(mask) == 0:
                    continue
                
                group_preds = preds[mask]
                group_targets = targets[mask]
                
                mse = np.mean((group_preds - group_targets) ** 2)
                mae = np.mean(np.abs(group_preds - group_targets))
                
                seed_metrics[group_cat]["mse"].append(mse)
                seed_metrics[group_cat]["mae"].append(mae)
                
            # Overall metrics
            overall_mse = np.mean((preds - targets) ** 2)
            overall_mae = np.mean(np.abs(preds - targets))
            seed_metrics["Overall"]["mse"].append(overall_mse)
            seed_metrics["Overall"]["mae"].append(overall_mae)

        # Check if any seed was processed
        processed_seeds_count = len(seed_metrics["Overall"]["mse"])
        if processed_seeds_count == 0:
            print(f"  [-] Warning: No seeds processed for {model_name}. skipping.")
            continue
            
        all_model_results[disp_name] = seed_metrics
        
        # Print individual model table
        individual_results = []
        for group in list(REGIME_GROUPS.keys()) + ["Overall"]:
            mses = seed_metrics[group]["mse"]
            maes = seed_metrics[group]["mae"]
            
            mean_mse = np.mean(mses) if len(mses) > 0 else 0.0
            std_mse = np.std(mses) if len(mses) > 0 else 0.0
            mean_mae = np.mean(maes) if len(maes) > 0 else 0.0
            std_mae = np.std(maes) if len(maes) > 0 else 0.0
            
            mse_str = f"{mean_mse:.6f} ± {std_mse:.6f}" if len(mses) > 1 else f"{mean_mse:.6f}"
            mae_str = f"{mean_mae:.6f} ± {std_mae:.6f}" if len(maes) > 1 else f"{mean_mae:.6f}"
            
            individual_results.append({
                "Regime Category": group,
                "MSE (mean ± std)": mse_str,
                "MAE (mean ± std)": mae_str
            })
        df_ind = pd.DataFrame(individual_results)
        print("\n" + "=" * 70)
        print(f"STRATIFIED BENCHMARK PERFORMANCE: {disp_name} (Processed {processed_seeds_count} seeds)")
        print("=" * 70)
        print(dataframe_to_markdown(df_ind))
        print("=" * 70)

    # 6. Generate Combined Table 1
    if len(all_model_results) == 0:
        print("[-] No models were successfully evaluated.")
        return None

    print("\n" + "=" * 120)
    print("FINAL COMBINED STRATIFIED BENCHMARK PERFORMANCE (TABLE 1 REPRODUCTION)")
    print("=" * 120)

    # Columns of Table 1: Model, Overall MSE, Overall MAE, Complex MSE, Complex MAE, Stable MSE, Stable MAE, Oscillatory MSE, Oscillatory MAE, Monotonic MSE, Monotonic MAE
    headers = ["Model", "Overall MSE", "Overall MAE", "Complex MSE", "Complex MAE", "Stable MSE", "Stable MAE", "Oscillatory MSE", "Oscillatory MAE", "Monotonic MSE", "Monotonic MAE"]
    table_rows = []

    for group_name, display_list in MODEL_ORDER:
        # Add section header
        table_rows.append([f"**{group_name}**"] + [""] * 10)
        
        has_items_in_group = False
        for disp in display_list:
            if disp in all_model_results:
                has_items_in_group = True
                metrics = all_model_results[disp]
                row = [disp]
                
                for cat in ["Overall", "Complex", "Stable", "Oscillatory", "Monotonic"]:
                    mses = metrics[cat]["mse"]
                    maes = metrics[cat]["mae"]
                    
                    mean_mse = np.mean(mses) if len(mses) > 0 else 0.0
                    std_mse = np.std(mses) if len(mses) > 0 else 0.0
                    mean_mae = np.mean(maes) if len(maes) > 0 else 0.0
                    std_mae = np.std(maes) if len(maes) > 0 else 0.0
                    
                    mse_str = f"{mean_mse:.4f}±{std_mse:.3f}" if len(mses) > 1 else f"{mean_mse:.4f}"
                    mae_str = f"{mean_mae:.4f}±{std_mae:.3f}" if len(maes) > 1 else f"{mean_mae:.4f}"
                    row.append(mse_str)
                    row.append(mae_str)
                table_rows.append(row)
                
        # If none of the predefined models in this group were found, search for any discovered models belonging to this group
        if not has_items_in_group:
            # check if there is any other model belonging to this group
            for disp, metrics in all_model_results.items():
                _, g_name = get_display_name_and_group(disp)
                if g_name == group_name and disp not in display_list:
                    row = [disp]
                    for cat in ["Overall", "Complex", "Stable", "Oscillatory", "Monotonic"]:
                        mses = metrics[cat]["mse"]
                        maes = metrics[cat]["mae"]
                        
                        mean_mse = np.mean(mses) if len(mses) > 0 else 0.0
                        std_mse = np.std(mses) if len(mses) > 0 else 0.0
                        mean_mae = np.mean(maes) if len(maes) > 0 else 0.0
                        std_mae = np.std(maes) if len(maes) > 0 else 0.0
                        
                        mse_str = f"{mean_mse:.4f}±{std_mse:.3f}" if len(mses) > 1 else f"{mean_mse:.4f}"
                        mae_str = f"{mean_mae:.4f}±{std_mae:.3f}" if len(maes) > 1 else f"{mean_mae:.4f}"
                        row.append(mse_str)
                        row.append(mae_str)
                    table_rows.append(row)

    # Print markdown table
    df_combined = pd.DataFrame(table_rows, columns=headers)
    markdown_table = dataframe_to_markdown(df_combined)
    print(markdown_table)
    print("=" * 120)

    # Save results to a CSV / MD file under save_path_dir
    os.makedirs(save_path_dir, exist_ok=True)
    summary_md_path = os.path.join(save_path_dir, "benchmark_table_1.md")
    with open(summary_md_path, "w", encoding="utf-8") as f:
        f.write("# Final Benchmark Stratified Performance (Table 1)\n\n")
        f.write(markdown_table)
        f.write("\n")
    print(f"[+] Master benchmark summary table saved to: {summary_md_path}\n")

    return df_combined

# Run the evaluation suite on our predictions targeting ONLY Seed 53
evaluate_model_suite(
    save_path_dir="./results",
    seeds=[53],
    data_dir="./SysBio-Traj",
    load_name="SysBio-Traj_index.csv"
)
