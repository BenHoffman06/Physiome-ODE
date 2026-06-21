# RegimeFlow & SysBio-Traj formatting guide for Physiome-ODE Models

This guide outlines the technical requirements, directory layout, and workflows required to adapt compiled **Physiome-ODE** (CellML) models into the **SysBio-Traj** dataset format. This format is required to train and evaluate the **RegimeFlow** trajectory prediction framework (accepted at **ICML 2026**).

---

## 1. Directory Structure Layout

To integrate your CellML models, they must be formatted into the standardized directory layout of `SysBio-Traj`:

```text
SysBio-Traj-CellML/
├── README.md
├── SysBio-Traj_index.csv              # Global index of simulated models
├── scripts/
│   └── simulate_cellml.py             # Trajectory reproduction script
└── Data/
    ├── <model_id>/                    # Unique model identifier (e.g., dupont_1991a)
    │   ├── <model_name>.csv           # Simulated multivariate trajectory (512 time points)
    │   ├── <model_name>.cellml         # Raw source XML model definition
    │   ├── initial_conditions.json    # Initial values & parameter values used for simulation
    │   └── <model_name>_conditions.json # Regime annotations & bounds per state variable
```

---

## 2. File Requirements & Schema Specifications

### A. Global Index (`SysBio-Traj_index.csv`)
A CSV cataloging all simulated systems.
- **Columns**: `model_id`, `model_name`, `time_start`, `time_end`, `time_span`
- **Example**:
  ```csv
  model_id,model_name,time_start,time_end,time_span
  dupont_1991a,dupont_1991a,0,30,30
  ```

### B. Curated Initial State (`initial_conditions.json`)
This file contains the parameter values (constants) and state variables (initial states) used for simulation.
- **Why it matters**: It separates parameterization from code, enabling clean reproduction of the exact CSV trajectory.
- **Format**:
  ```json
  {
    "states": {
      "Z": 0.52,
      "Y": 0.93
    },
    "parameters": {
      "v0": 1.0,
      "v1": 7.3,
      "beta": 0.6,
      "VM2": 65.0,
      "VM3": 500.0,
      "KR": 2.0,
      "KA": 0.9,
      "kf": 1.0,
      "k": 10.0,
      "K2": 1.0,
      "n": 2.0,
      "m": 2.0,
      "p": 4.0
    }
  }
  ```
- **How to create**: Extract the defaults from `initConsts()` inside the OpenCOR-generated Python script.

### C. Simulated Trajectory (`<model_name>.csv`)
- **Format**: CSV with `time` as the first column, followed by one column per state variable/species (e.g., `Z`, `Y`).
- **Length**: Exactly **512 uniformly sampled points** from `time_start` to `time_end`.
- **How to create**: Use the reproduction script `simulate_cellml.py` to run the numerical simulation over a linear time-grid (`np.linspace(start, end, 512)`).

### D. Regime Annotations (`<model_name>_conditions.json`)
Stores the dynamic regime classification for **each species/state variable** in the simulation.
- **Format**:
  ```json
  {
    "Z": {
      "trajectory_type": 3,
      "trajectory_type_name": "oscillation",
      "bounds": [0.05, 1.25],
      "period": 42.0
    },
    "Y": {
      "trajectory_type": 0,
      "trajectory_type_name": "directly_stable",
      "bounds": [0.1, 0.95],
      "period": 0.0
    }
  }
  ```

> [!IMPORTANT]
> **Manual Curation of Regimes**:
> Naive heuristic rules or AI classifications of biological regimes are frequently inaccurate. They often misclassify decaying oscillations as stable states or confuse slow monotonic changes with oscillations. 
> To ensure high-quality dataset annotations:
> 1. Calculate the `bounds` (`[min(val), max(val)]`) programmatically from the simulated CSV trajectory.
> 2. Calculate the `period` using signal-processing methods (like peak detection or FFT).
> 3. **Manually curate or visually inspect** the regime labels (`trajectory_type`) to map them to the six-class RegimeFlow taxonomy:
>    - `0`: `directly_stable` (*complex* in paper)
>    - `1`: `inc_stable` (*increasing-stable*)
>    - `2`: `dec_stable` (*decaying-stable*)
>    - `3`: `oscillation`
>    - `4`: `increasing` (*monotonic increasing*)
>    - `5`: `decreasing` (*monotonic decreasing*)

---

## 3. Simulating and Reproducing Trajectories

To reproduce trajectories from the compiled CellML source files and curated initial conditions, use the provided `scripts/simulate_cellml.py` helper.

### CLI Usage Instructions
```bash
python scripts/simulate_cellml.py \
  --model-dir Data/dupont_1991a \
  --model-name dupont_1991a \
  --start-time 0 \
  --end-time 30 \
  --num-timepoints 512 \
  --use-ic-json
```

### Script Parameters
* `--model-dir`: Path to the directory containing `<model_name>_wrapped.py` and `initial_conditions.json`.
* `--model-name`: Base name of the model.
* `--start-time` / `--end-time`: Duration range for the ODE solver.
* `--num-timepoints`: Number of points to sample (usually `512` for RegimeFlow).
* `--use-ic-json`: Overrides default state/parameter values using the values inside `initial_conditions.json`.
* `--output`: (Optional) Custom path for the output CSV file. Defaults to `model_dir/<model_name>.csv`.

---

## 4. Next Steps

For the full end-to-end pipeline — from model compilation through to publishing on Hugging Face — see the [CellML Integration & Publishing Roadmap](./CellML_Integration_Roadmap.md).
