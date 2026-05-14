# RegimeFlow (ICML Submission)

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Framework](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![Conference](https://img.shields.io/badge/ICML-Under%20Review-green)](https://icml.cc/)

This repository contains the implementation of **RegimeFlow**, a *regime-aware* flow matching framework for probabilistic forecasting of biological trajectories across systems.

The project is built on top of the training/evaluation infrastructure of **[Time-Series-Library](https://github.com/thuml/Time-Series-Library)** and uses **[Hydra](https://hydra.cc/)** for configuration management.

**Highlights**
- **End-to-end training and evaluation pipeline** for biological trajectory forecasting.
- **Probabilistic forecasting models** including RegimeFlow, TSFlow, and diffusion-based baselines.
- **Point forecasting baselines** for deterministic comparison.
- **Toy dataset included** for quick smoke tests and debugging.
- **Reusable launch scripts** under `scripts/` for faster and more reproducible runs.

> **Anonymity note**  
> Author names and affiliations are intentionally omitted to preserve double-blind review.

---

## Repository Structure

```text
.
├── data/
│   └── ToyData/                  # Small bundled subset for quick checks
├── dataset/                      # Dataset construction and train/val/test splits
├── exp/
│   ├── train_bioTFM.py           # Main training / evaluation entry point
│   └── configs/                  # Hydra configs
│       ├── config.yaml           # Main config for full-dataset experiments
│       ├── config_toy.yaml       # Config template for toy experiments
│       └── model/
│           ├── PointForecasting/
│           └── ProbabilityForecasting/
├── models/
│   ├── FlowMatching/             # RegimeFlow and TSFlow variants
│   ├── Diffusion/                # Diffusion baselines
│   └── PointForecasting/         # Deterministic / zero-shot baselines
└── scripts/                      # Convenience launch scripts
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

This repository depends on `mamba-ssm` (v2.x). If your local CUDA compiler is incompatible with the CUDA version used by PyTorch, you may see ABI or `undefined symbol` errors.

If that happens, reinstall the low-level dependencies from source:

```bash
pip install causal-conv1d>=1.4.0 --no-binary causal-conv1d --force-reinstall --no-cache-dir
pip install mamba-ssm>=2.2.6 --no-binary mamba-ssm --force-reinstall --no-cache-dir
```

Before doing so, make sure `nvcc --version` is available and compatible with your PyTorch build.

---

## Dataset Setup

### Toy dataset

A small example dataset is bundled under `data/ToyData/`.

Use it for:
- sanity-checking the data pipeline,
- verifying that training/evaluation commands run end-to-end,
- quick debugging before launching full experiments.

### Full dataset

The full biological dataset is **not** included in this repository due to size and review constraints.

We will release the full dataset after paper acceptance. Thank you for your understanding.

For full experiments, you need to provide:
- `data.data_dir`: path to the dataset root,
- `data.load_name`: metadata CSV filename,
- `save_path_dir`: output directory for logs/checkpoints.

### Important note on local paths

Some checked-in config files contain machine-specific placeholder paths used during development.  
If a command does not work out of the box, explicitly override these fields from the command line:

- `data.data_dir`
- `data.load_name`
- `save_path_dir`
- `hardware.devices`

---

## Quick Start

All commands below are meant to be run from the **repository root**.

### 0. Fastest start: use the provided launch scripts

If you want to get started quickly, the easiest entry point is the `scripts/` folder. These launchers already package the common Hydra overrides used in our experiments, so after you set your local paths/configs, you can start runs with a single command.

Examples:

```bash
# RegimeFlow on the toy setting
bash scripts/exp_train_FM_toy.bash 500 RegimeFlow 0 1024 50

# Standard point-forecasting baseline on the toy setting
bash scripts/exp_train_Point_toy.bash 100 iTransformer 0 64 10 "53"

# Chronos zero-shot evaluation on the toy setting
bash scripts/exp_train_Point_chronos_toy.bash 1 Chronos 0 64 1 "53" /path/to/local/chronos-checkpoint
```

This is the recommended way to reproduce the common setups in this repository with minimal command-line editing.

### 1. Probabilistic forecasting on the toy dataset

A minimal RegimeFlow run:

```bash
WANDB_MODE=offline python exp/train_bioTFM.py \
  -cp exp/configs \
  -cn config_toy \
  model=ProbabilityForecasting/RegimeFlow \
  data.data_dir=./data/ToyData \
  data.load_name=example_info.csv \
  data.data_type=BioTFM \
  save_path_dir=./outputs \
  experiment_name=toy_RegimeFlow \
  seed=53 \
  training.max_epochs=500 \
  training.warmup_epochs=0 \
  training.check_val_every_n_epoch=50 \
  training.limit_val_batches=1.0 \
  data.batch_size=1024 \
  data.num_workers=0 \
  hardware.devices=[0]
```

To switch to another probabilistic baseline, only change the `model=` field. For example:

```bash
model=ProbabilityForecasting/TSFlow_PE
model=ProbabilityForecasting/TSDiff_regime
model=ProbabilityForecasting/CSDI_regime
```

### 2. Full-dataset training

```bash
WANDB_MODE=offline python exp/train_bioTFM.py \
  -cp exp/configs \
  -cn config \
  model=ProbabilityForecasting/RegimeFlow \
  data.data_dir=/path/to/full/dataset \
  data.load_name=system_info.csv \
  data.data_type=BioTFM \
  save_path_dir=/path/to/outputs \
  experiment_name=full_RegimeFlow_seed53 \
  seed=53 \
  hardware.devices=[0]
```

---

## Evaluation

To evaluate a trained checkpoint:

```bash
WANDB_MODE=offline python exp/train_bioTFM.py \
  -cp exp/configs \
  -cn config_toy \
  model=ProbabilityForecasting/RegimeFlow \
  data.data_dir=./data/ToyData \
  data.load_name=example_info.csv \
  data.data_type=BioTFM \
  save_path_dir=./outputs \
  experiment_name=toy_eval \
  test_only=true \
  ckpt_path=/path/to/checkpoint.ckpt \
  hardware.devices=[0]
```

If the checkpoint contains `ema_state_dict`, the evaluation script will automatically use EMA weights.

---

## Point Forecasting Baselines

Standard point forecasting baselines are configured under:

- `PointForecasting/iTransformer`
- `PointForecasting/PatchTST`
- `PointForecasting/DLinear`
- `PointForecasting/S_Mamba`
- `PointForecasting/BiMamba4TS`
- `PointForecasting/TimeMixer`
- `PointForecasting/TimeXer`

Example:

```bash
WANDB_MODE=offline python exp/train_bioTFM.py \
  -cp exp/configs \
  -cn config_toy \
  model=PointForecasting/iTransformer \
  data.data_dir=./data/ToyData \
  data.load_name=example_info.csv \
  data.data_type=PointTrajectory \
  save_path_dir=./outputs \
  experiment_name=toy_iTransformer \
  seed=53 \
  training.max_epochs=100 \
  data.batch_size=64 \
  hardware.devices=[0]
```

---

## Chronos Baseline

Chronos is integrated through the point-forecasting pipeline.

At the moment, the provided Chronos launcher is set up for **zero-shot evaluation** rather than standard fine-tuning.

Example:

```bash
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 WANDB_MODE=offline python exp/train_bioTFM.py \
  -cp exp/configs \
  -cn config_toy \
  model=PointForecasting/Chronos \
  data.data_dir=./data/ToyData \
  data.load_name=example_info.csv \
  data.data_type=PointTrajectory \
  save_path_dir=./outputs \
  experiment_name=toy_Chronos \
  seed=53 \
  test_only=true \
  test_without_ckpt=true \
  data.batch_size=64 \
  hardware.devices=[0] \
  model.model.args.pretrained_model_path=/path/to/local/chronos-checkpoint \
  model.model.args.local_files_only=true
```

If you use a local checkpoint directory, it should contain at least:
- `config.json`
- `model.safetensors`

Convenience scripts are also available:
- `scripts/exp_train_Point_chronos_toy.bash`
- `scripts/exp_train_Point_chronos.bash`

---

## Convenience Scripts

The `scripts/` directory contains helper launchers for common experiments.

Examples:

- `scripts/exp_train_FM_toy.bash`
- `scripts/exp_train_FM.bash`
- `scripts/exp_train_Point_toy.bash`
- `scripts/exp_train_Point.bash`
- `scripts/exp_train_Point_chronos_toy.bash`

Please note:
- some scripts assume you have already edited the config files for your local paths;
- some scripts launch multiple seeds;
- `exp_train_FM_toy.bash` currently uses the seed list defined inside the script.

---

## Hydra Configuration

This project uses Hydra for configuration overrides.

Useful flags:
- `-cp`: config directory
- `-cn`: config name

Typical overrides:

```bash
training.max_epochs=500
training.check_val_every_n_epoch=10
data.batch_size=1024
hardware.devices=[0]
```

Model configs are organized under:
- `exp/configs/model/ProbabilityForecasting/`
- `exp/configs/model/PointForecasting/`

---

## Acknowledgements

We thank the authors of the following repository for their open-source contribution, which serves as the basis of our training/evaluation infrastructure:

- **Time-Series-Library:** https://github.com/thuml/Time-Series-Library

---

## Citation

A citation entry will be added after publication.
