# RegimeFlow (ICML Submission)

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Framework](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![Conference](https://img.shields.io/badge/ICML-Under%20Review-green)](https://icml.cc/)

**RegimeFlow** is a regime-aware flow matching framework for probabilistic forecasting of biological trajectories across dynamical systems.

This repository provides the training and evaluation code used for the full biological trajectory benchmark. It builds on the training/evaluation infrastructure of **[Time-Series-Library](https://github.com/thuml/Time-Series-Library)** and uses **[Hydra](https://hydra.cc/)** for reproducible configuration management.

**Highlights**
- End-to-end full-dataset training and evaluation pipeline.
- Probabilistic forecasting models, including RegimeFlow, TSFlow, and diffusion-based baselines.
- Point forecasting baselines for deterministic comparison.
- Script-based experiment launchers for common reproduction runs.
- A full dataset release path reserved for Hugging Face.

> **Anonymity note**  
> Author names and affiliations are intentionally omitted to preserve double-blind review.

---

## Repository Structure

```text
.
├── dataset/                      # Dataset loading, filtering, and train/val/test splits
├── exp/
│   ├── train_bioTFM.py           # Main training / evaluation entry point
│   └── configs/                  # Hydra configs
│       ├── config.yaml           # Main full-dataset experiment config
│       └── model/
│           ├── PointForecasting/
│           └── ProbabilityForecasting/
├── models/
│   ├── FlowMatching/             # RegimeFlow and TSFlow variants
│   ├── Diffusion/                # Diffusion baselines
│   └── PointForecasting/         # Deterministic / zero-shot baselines
├── scripts/                      # Full-dataset launch scripts
└── Materials/                    # Optional pretrained model assets and references
```

---

## Installation

The project has been tested on the following environment:

- **OS:** Ubuntu 22.04+
- **Python:** 3.10.19
- **PyTorch:** 2.9.1
- **CUDA toolkit (`nvcc`):** 12.4
- **GPU:** NVIDIA RTX A6000
- **mamba-ssm:** 2.2.6

### 1. Create the environment

```bash
conda env create -f environment.yml
conda activate mambaseries
```

### 2. Rebuild `mamba-ssm` if needed

This repository depends on `mamba-ssm` v2.x. If your local CUDA compiler is incompatible with the CUDA version used by PyTorch, you may see ABI or `undefined symbol` errors.

If that happens, reinstall the low-level dependencies from source:

```bash
pip install causal-conv1d>=1.4.0 --no-binary causal-conv1d --force-reinstall --no-cache-dir
pip install mamba-ssm>=2.2.6 --no-binary mamba-ssm --force-reinstall --no-cache-dir
```

Before doing so, make sure `nvcc --version` is available and compatible with your PyTorch build.

---

## Dataset

The full biological trajectory dataset will be released on Hugging Face:

```text
https://huggingface.co/datasets/<ORG_OR_USER>/<DATASET_REPO>
```

After release, download it with:

```bash
huggingface-cli download <ORG_OR_USER>/<DATASET_REPO> \
  --repo-type dataset \
  --local-dir /path/to/SysBio-Traj
```

Expected local layout:

```text
/path/to/SysBio-Traj/
├── system_info.csv
└── Data/
    └── <model_id>/
        ├── <model_name>.csv
        └── <model_name>_conditions.json
```

The metadata CSV must contain at least:

- `model_id`
- `model_name`

The loader constructs each trajectory path as:

```text
<data.data_dir>/Data/<model_id>/<model_name>.csv
```

For each trajectory CSV, the corresponding condition file should be placed next to it with the suffix `_conditions.json`.

---

## Configure Paths

Before launching experiments, update the full-dataset config:

```yaml
# exp/configs/config.yaml
save_path_dir: /path/to/outputs

data:
  data_dir: /path/to/SysBio-Traj
  load_name: system_info.csv

hardware:
  devices: [0]
```

These fields control:

- `data.data_dir`: root directory of the downloaded dataset.
- `data.load_name`: metadata CSV filename under `data.data_dir`.
- `save_path_dir`: output root for checkpoints, logs, predictions, and Hydra outputs.
- `hardware.devices`: GPU index list used by PyTorch Lightning.

If your metadata file is named differently, also update the `load_name` variable near the top of the relevant launch script:

- `scripts/exp_train_FM.bash`
- `scripts/exp_train_Point.bash`
- `scripts/exp_train_Point_chronos.bash`

The current scripts assume `load_name="system_info.csv"` and read `data.data_dir` from `exp/configs/config.yaml`.

---

## Quick Start

All commands should be run from the repository root.

### Option A: launch with scripts

The fastest way to reproduce common experiments is to use the provided full-dataset scripts.

RegimeFlow:

```bash
bash scripts/exp_train_FM.bash 500 RegimeFlow 0 1024 50 "53"
```

Other probabilistic baselines:

```bash
bash scripts/exp_train_FM.bash 500 TSFlow_PE 0 1024 50 "53"
bash scripts/exp_train_FM.bash 500 TSDiff_regime 0 1024 50 "53"
bash scripts/exp_train_FM.bash 500 CSDI_regime 0 1024 50 "53"
```

Point forecasting baseline:

```bash
bash scripts/exp_train_Point.bash 100 iTransformer 0 64 10 "53"
```

Chronos zero-shot evaluation:

```bash
bash scripts/exp_train_Point_chronos.bash 1 Chronos 0 64 1 "53" /path/to/local/chronos-checkpoint
```

Script arguments:

```text
exp_train_FM.bash <max_epochs> <model_name> <gpu_id> <batch_size> <eval_freq> "<seeds>"
exp_train_Point.bash <max_epochs> <model_name> <gpu_id> <batch_size> <eval_freq> "<seeds>"
exp_train_Point_chronos.bash <max_epochs> <model_name> <gpu_id> <batch_size> <eval_freq> "<seeds>" <local_model_dir> [offline_mode]
```

For multiple seeds, pass a quoted space-separated list, for example `"53 25 81"`.

### Option B: launch with Hydra directly

Use direct Hydra commands when you want all paths and overrides visible in the command line.

```bash
WANDB_MODE=offline python exp/train_bioTFM.py \
  -cp ./configs \
  -cn config \
  model=ProbabilityForecasting/RegimeFlow \
  data.data_dir=/path/to/SysBio-Traj \
  data.load_name=system_info.csv \
  data.data_type=BioTFM \
  save_path_dir=/path/to/outputs \
  experiment_name=full_RegimeFlow_seed53 \
  seed=53 \
  training.max_epochs=500 \
  training.warmup_epochs=0 \
  training.check_val_every_n_epoch=50 \
  training.limit_val_batches=1.0 \
  data.batch_size=1024 \
  data.num_workers=0 \
  hardware.devices=[0]
```

To switch models, change only the `model=` override:

```bash
model=ProbabilityForecasting/RegimeFlow
model=ProbabilityForecasting/TSFlow_PE
model=ProbabilityForecasting/TSDiff_regime
model=ProbabilityForecasting/CSDI_regime
model=PointForecasting/iTransformer
```

---

## Evaluation

To evaluate a trained checkpoint on the full dataset:

```bash
WANDB_MODE=offline python exp/train_bioTFM.py \
  -cp ./configs \
  -cn config \
  model=ProbabilityForecasting/RegimeFlow \
  data.data_dir=/path/to/SysBio-Traj \
  data.load_name=system_info.csv \
  data.data_type=BioTFM \
  save_path_dir=/path/to/outputs \
  experiment_name=full_RegimeFlow_eval \
  test_only=true \
  ckpt_path=/path/to/checkpoint.ckpt \
  hardware.devices=[0]
```

If the checkpoint contains `ema_state_dict`, the evaluation script automatically uses EMA weights.

---

## Supported Models

Probabilistic forecasting configs:

- `ProbabilityForecasting/RegimeFlow`
- `ProbabilityForecasting/TSFlow_PE`
- `ProbabilityForecasting/TSFlow_PE_regime`
- `ProbabilityForecasting/TSDiff_regime`
- `ProbabilityForecasting/CSDI_regime`

Point forecasting configs:

- `PointForecasting/iTransformer`
- `PointForecasting/PatchTST`
- `PointForecasting/DLinear`
- `PointForecasting/S_Mamba`
- `PointForecasting/BiMamba4TS`
- `PointForecasting/TimeMixer`
- `PointForecasting/TimeXer`
- `PointForecasting/Chronos`

Model configs are located under:

- `exp/configs/model/ProbabilityForecasting/`
- `exp/configs/model/PointForecasting/`

---

## Chronos Baseline

Chronos is integrated through the point-forecasting pipeline and is currently used for zero-shot evaluation.

When using a local Chronos checkpoint, the directory should contain:

- `config.json`
- `model.safetensors`

Example:

```bash
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 WANDB_MODE=offline python exp/train_bioTFM.py \
  -cp ./configs \
  -cn config \
  model=PointForecasting/Chronos \
  data.data_dir=/path/to/SysBio-Traj \
  data.load_name=system_info.csv \
  data.data_type=PointTrajectory \
  save_path_dir=/path/to/outputs \
  experiment_name=full_Chronos \
  seed=53 \
  test_only=true \
  test_without_ckpt=true \
  data.batch_size=64 \
  hardware.devices=[0] \
  model.model.args.pretrained_model_path=/path/to/local/chronos-checkpoint \
  model.model.args.local_files_only=true
```

---

## Hydra Configuration

Useful Hydra flags:

- `-cp`: config directory, resolved relative to `exp/train_bioTFM.py` for this entry point.
- `-cn`: config name.

Common overrides:

```bash
data.data_dir=/path/to/SysBio-Traj
data.load_name=system_info.csv
save_path_dir=/path/to/outputs
training.max_epochs=500
training.check_val_every_n_epoch=10
data.batch_size=1024
hardware.devices=[0]
```

The main config file for full-dataset experiments is:

```text
exp/configs/config.yaml
```

---

## Outputs

Outputs are organized under `save_path_dir`:

```text
<save_path_dir>/
├── checkpoints/<experiment_name>/<seed>/
├── logs/<experiment_name>/<seed>/
├── outputs/<experiment_name>/<seed>/
└── predictions/<experiment_name>/<seed>/
```

Final test metrics are saved as CSV files in the checkpoint directory.

---

## Acknowledgements

We thank the authors of the following repository for their open-source contribution, which serves as the basis of our training/evaluation infrastructure:

- **Time-Series-Library:** https://github.com/thuml/Time-Series-Library

---

## Citation

A citation entry will be added after publication.
