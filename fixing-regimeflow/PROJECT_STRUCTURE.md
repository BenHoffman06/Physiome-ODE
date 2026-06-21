# RegimeFlow: Project & Dataset Structure

This document outlines the architecture, directory structure, dataset layout, and training pipeline of the **RegimeFlow** framework. RegimeFlow is a regime-aware flow matching framework for the probabilistic forecasting of biological trajectories across thousands of dynamical systems (accepted at **ICML 2026**).

---

## 1. Dataset Layout & Formatting (`SysBio-Traj`)

The companion dataset for this project is **SysBio-Traj** (hosted on Hugging Face at `HengRao/SysBio-Traj`). It contains simulated trajectories and metadata for **1,050 biological dynamical systems** (derived from SBML models simulated via Tellurium).

### Directory Hierarchy
```text
SysBio-Traj/
├── README.md
├── SysBio-Traj_index.csv
├── scripts/
│   └── simulate_sbml.py
└── Data/
    ├── <model_id>/                 # e.g., BIOMD0000000013, MODEL2408...
    │   ├── <model_name>.csv        # Simulated multivariate trajectory
    │   ├── <model_name>.xml        # Source SBML model in XML format
    │   ├── initial_conditions.json # Curated initial state for reproduction
    │   └── <model_name>_conditions.json # Per-species regime labels and bounds
    └── ...
```

### Component Files Details

1. **`SysBio-Traj_index.csv` (Global Metadata Index)**
   Stores model information to index and locate system trajectories.
   * Columns: `model_id`, `model_name`, `time_start`, `time_end`, `time_span`.

2. **`<model_name>.csv` (Multivariate Trajectory Data)**
   * Format: CSV file containing `time` (first column) and one column per biological species.
   * Trajectory Length: Exactly **512** uniformly sampled time points.

3. **`<model_name>_conditions.json` (Regime Annotations & Metrics)**
   Maps each species variable to its biological regime type and boundaries:
   * `trajectory_type`: Numeric regime label (0 to 5) used by RegimeFlow.
   * `trajectory_type_name`: String representations of the six-class regime taxonomy:
     * `directly_stable` (Paper: *complex*)
     * `inc_stable` (Paper: *increasing-stable*)
     * `dec_stable` (Paper: *decaying-stable*)
     * `oscillation` (Paper: *oscillation*)
     * `increasing` (Paper: *monotonic increasing*)
     * `decreasing` (Paper: *monotonic decreasing*)
   * `bounds`: `[min_val, max_val]` observed across the trajectory for the species.
   * `period`: Calculated period in sample-index units.

4. **`initial_conditions.json`**
   * Curated initial species concentrations and rates for deterministic trajectory reproduction.

---

## 2. Project Directory Structure

```text
RegimeFlow/
├── dataset/             # Custom PyTorch Datasets and data splits
├── models/              # Neural network implementations (Flow Matching, Point, Diffusion)
├── layers/              # Modular neural network layers and encoding blocks
├── exp/                 # Experiment execution scripts and configurations
│   ├── configs/         # Hydra configuration files
│   └── train_bioTFM.py  # Main training and evaluation entry point
├── scripts/             # Bash wrappers for executing training runs
├── data_provider/       # Baseline data loader factories
├── utils/               # Loss functions, metrics, augmentations, and EMA helpers
├── PROJECT_STRUCTURE.md # This architecture overview
└── environment.yml      # Conda environment specifications
```

### Key Modules

### `dataset/`
* `BaseBioDataset.py`: Implements `SingleBioSeriesDataset` to load a single CSV trajectory, filter invalid variables, build sliding time-windows, and extract categorical system conditions.
* `BioSeries.py`: Implements `MultiBioSeriesDataset` which aggregates multiple single biological series into a single dataset, applies forward log/min-max transforms, and constructs standard collation wrappers.
* `BioFMSeries.py`: Creates flow-matching datamodules, incorporating auto-regressive (AR) training features.
* `get_train_val_test.py`: Implements two partitioning styles:
  * **Standard Split (`get_train_val_test_splits`)**: Index-based split where train, val, and test subsets share the same systems but utilize different time windows.
  * **Out-of-Distribution Split (`get_train_val_test_splits_ood`)**: File-based split where biological systems (models) are split into disjoint sets, ensuring the model is evaluated on completely unseen biological systems (OOD).
* `data_utils.py`: Data filtering utility functions. It enforces:
  1. Removal of negative concentration values.
  2. Filtering of values above $10^9$ (NaN/inf values).
  3. Pruning of almost-constant variables (relative range $< 10^{-3}$ and unique values ratio $< 1\%$).

### `models/`
* `FlowMatching/`:
  * `RegimeFlow/`: The primary framework codebase. Incorporates regime-conditional vector field regression layers (`bio_cond_layers.py`), backbone flow network (`backbone.py`), and ODE solvers (`RegimeFlow.py`).
  * `TSFlow/`: Time-series Flow Matching baseline.
* `Diffusion/`:
  * `CSDI/`: Conditional Spatio-Temporal Diffusion baseline.
  * `TSDiff/`: Time-Series Diffusion baseline.
* `PointForecasting/`:
  * Wrappers (`PointForecasting.py`) for deterministic baselines.
  * Supported models: `iTransformer`, `PatchTST`, `DLinear`, `S_Mamba`, `BiMamba4TS`, `TimeMixer`, `TimeXer`, `NSformer`, and `Chronos` (Zero-shot LLM forecaster).

### `layers/`
* Houses standard sequence encoding, attention blocks, and recurrence layers:
  * `Embed.py`: Temporal, spatial, and value embeddings.
  * `SelfAttention_Family.py` / `AutoCorrelation.py` / `FourierCorrelation.py`: Attention mechanisms.
  * `Mamba_EncDec.py`: State Space model encoders.

---

## 3. Training & Evaluation Pipeline

The framework uses **Hydra** for configuration management and **PyTorch Lightning** for training orchestration.

### Execution Workflow
1. Configs are defined under `exp/configs/config.yaml` and model-specific configs under `exp/configs/model/`.
2. `exp/train_bioTFM.py` initializes:
   * The training dataset (applying log or minmax transformations to concentrations and times).
   * The Lightning module (e.g. `RegimeFlow`, `TSFlow_PE`, or standard Point models).
   * Callbacks (Early Stopping, Checkpointing, and **Exponential Moving Average (EMA)**).
   * Logger (Weights & Biases).
3. Test-only execution mode (`test_only=true`) can run model evaluations directly from a checkpoint or run zero-shot inference (e.g., Chronos).
