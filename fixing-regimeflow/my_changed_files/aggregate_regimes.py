import os
import numpy as np
import pandas as pd
import torch
from tqdm import tqdm
import inspect
import warnings

# Suppress PyTorch tensor warnings to keep your console clean
warnings.filterwarnings('ignore')

# --- 1. CONFIGURATION ---
NPZ_PATH = "./results/predictions/CSDI_regime_seed25/25/test_predictions.npz"
INDEX_PATH = "./SysBio-Traj/SysBio-Traj_index.csv"
DATA_ROOT = "./SysBio-Traj/Data"

print(f"=== Loading {NPZ_PATH} ===")
if not os.path.exists(NPZ_PATH):
    raise FileNotFoundError(f"Could not find the predictions file at {NPZ_PATH}.")

data = np.load(NPZ_PATH)
preds = data['predictions']
trues = data['targets']
print(f"Loaded Predictions shape: {preds.shape} | Ground Truth shape: {trues.shape}")

# --- 2. CALCULATE METRICS ---
print("\n=== Calculating Per-Sample Metrics ===")
sample_mse = np.mean((preds - trues) ** 2, axis=(1, 2))
sample_mae = np.mean(np.abs(preds - trues), axis=(1, 2))

# --- 3. PANDAS INTERCEPTOR ---
original_read_csv = pd.read_csv
def patched_read_csv(*args, **kwargs):
    df = original_read_csv(*args, **kwargs)
    if 'Unnamed: 0' in df.columns: df = df.drop(columns=['Unnamed: 0'])
    if 'Time' in df.columns and 'time' not in df.columns: df = df.rename(columns={'Time': 'time'})
    if 'time' in df.columns: df = df[['time'] + [col for col in df.columns if col != 'time']]
    return df
pd.read_csv = patched_read_csv

# --- 4. LOCATE DATASET CLASS ---
print("\n=== Loading Dataset Class ===")
import dataset.BaseBioDataset as base_module

module_classes = [obj for name, obj in inspect.getmembers(base_module, inspect.isclass) 
                  if obj.__module__ == base_module.__name__]

# We want the class designed for single files since we will loop over the index manually
DatasetClass = next((c for c in module_classes if "Single" in c.__name__), module_classes[0])
print(f"Successfully located base dataset class: '{DatasetClass.__name__}'")

sig = inspect.signature(DatasetClass.__init__)
valid_params = list(sig.parameters.keys())

# --- 5. RECONSTRUCT MULTI-FILE DATASET FROM INDEX ---
print("\n=== Reconstructing Full Dataset from Index ===")
if not os.path.exists(INDEX_PATH):
    raise FileNotFoundError(f"Missing master index file at {INDEX_PATH}")

index_df = pd.read_csv(INDEX_PATH)

sample_to_model = []
sample_to_regime = []

for _, row in tqdm(index_df.iterrows(), total=len(index_df), desc="Processing Models"):
    model_id = str(row.get('model_id', ''))
    model_name = str(row.get('model_name', ''))
    
    file_name = model_name if model_name.endswith('.csv') else model_name + '.csv'
    file_path = os.path.join(DATA_ROOT, model_id, file_name)
    
    # Fallback search if the exact path structure isn't perfect
    if not os.path.exists(file_path):
        found = False
        for r, d, f in os.walk(DATA_ROOT):
            if file_name in f:
                file_path = os.path.join(r, file_name)
                found = True
                break
        if not found:
            continue
            
    # Setup parameters for this specific file
    dataset_kwargs = {}
    if 'data_path' in valid_params: dataset_kwargs['data_path'] = file_path
    if 'root_path' in valid_params: dataset_kwargs['root_path'] = os.path.dirname(file_path)
    if 'flag' in valid_params: dataset_kwargs['flag'] = "test"
    if 'input_window' in valid_params: dataset_kwargs['input_window'] = 96
    if 'output_window' in valid_params: dataset_kwargs['output_window'] = 256
    if 'stride' in valid_params: dataset_kwargs['stride'] = 16
    if 'transform_type' in valid_params: dataset_kwargs['transform_type'] = "minmax"
    
    try:
        sub_dataset = DatasetClass(**dataset_kwargs)
    except Exception:
        continue # Skip gracefully if a file fails to load
        
    # Extract samples and safely grab the regime
    for i in range(len(sub_dataset)):
        sample = sub_dataset[i]
        
        regime_val = 0
        for key in ['conditions', 'system_condition', 'condition']:
            if key in sample:
                cond = sample[key]
                # Safely flatten the vector to prevent IndexError
                if hasattr(cond, 'numel') and cond.numel() > 0:
                    vals = cond.view(-1).tolist()
                elif isinstance(cond, (list, tuple, np.ndarray)):
                    vals = list(cond)
                else:
                    vals = [cond]
                    
                # Dynamically grab the last relevant value based on actual length
                if len(vals) > 2: regime_val = vals[2]
                elif len(vals) > 1: regime_val = vals[1]
                elif len(vals) > 0: regime_val = vals[0]
                break
                
        sample_to_model.append(model_name)
        sample_to_regime.append(int(float(regime_val)))

# Restore pandas normal function
pd.read_csv = original_read_csv

# --- 6. AGGREGATE RESULTS BY MODEL AND REGIME ---
print(f"\nExtracted {len(sample_to_model)} samples. Generating report...")

min_len = min(len(sample_to_model), len(preds))
df = pd.DataFrame({
    'Model': sample_to_model[:min_len],
    'Regime': sample_to_regime[:min_len],
    'MSE': sample_mse[:min_len],
    'MAE': sample_mae[:min_len]
})

# 1. Calculate per-regime stats
regime_summary = df.groupby(['Regime']).agg({
    'MSE': ['mean', 'std'],
    'MAE': ['mean', 'std']
}).reset_index()
regime_summary.columns = ['Regime', 'MSE_mean', 'MSE_std', 'MAE_mean', 'MAE_std']

# 2. Calculate "Overall" stats
overall_stats = df.agg({
    'MSE': ['mean', 'std'],
    'MAE': ['mean', 'std']
}).transpose().reset_index()
overall_row = pd.DataFrame({
    'Regime': ['Overall'],
    'MSE_mean': [overall_stats.loc[0, 'mean']],
    'MSE_std': [overall_stats.loc[0, 'std']],
    'MAE_mean': [overall_stats.loc[1, 'mean']],
    'MAE_std': [overall_stats.loc[1, 'std']]
})

# 3. Combine them
final_report = pd.concat([overall_row, regime_summary], ignore_index=True)

print("\n=== Final Aggregated Performance (Table View) ===")
# Note: You can map these Regime integers to names (e.g., 0: Complex, 1: Stable) 
# if you have a dictionary mapping available.
print(final_report.to_string(index=False))

output_csv = "./results/predictions/CSDI_regime_seed25/25/regime_model_performance_table.csv"
final_report.to_csv(output_csv, index=False)