# RegimeFlow (ICML Submission)

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Framework](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![Conference](https://img.shields.io/badge/ICML-Under%20Review-green)](https://icml.cc/)

This repository contains the reference implementation of **RegimeFlow**, a *regime-aware* flow matching forecasting framework for cross systems biology trajectory prediction.

This codebase is built upon the training and evaluation infrastructure of the **[Time-Series-Library](https://github.com/thuml/Time-Series-Library)** (acknowledged below) and utilizes **Hydra** for flexible configuration management.

**Key Features:**
- **Generative Probabilistic Forecasting:** Implementations of RegimeFlow, Flow Matching, and Diffusion baselines.
- **Point Forecasting:** A suite of strong baselines (Transformer, MLP, and SSM architectures) for comprehensive comparison.

> **⚠️ Anonymity Note:** This README and the codebase intentionally omit author names and affiliations to comply with the double-blind review process.

---

## 📂 Repository Structure

```text
.
├── data/
│   └── ToyData/              # Small dataset included for sanity checks
├── exp/
│   ├── train_bioTFM.py       # Main entrypoint for training/testing
│   └── configs/              # Hydra configuration files
│       ├── config.yaml       # Template for full dataset experiments
│       ├── config_toy.yaml   # Configuration for the included toy dataset
│       └── model/            # Model-specific configs
│           ├── PointForecasting/       # e.g., iTransformer, PatchTST, Mamba
│           └── ProbabilityForecasting/ # e.g., RegimeFlow, TSFlow, Diffusion
├── models/
│   ├── FlowMatching/         # RegimeFlow & TSFlow implementations
│   └── Diffusion/            # Diffusion baselines (CSDI, TSDiff variants)
└── scripts/                  # Convenience bash launchers

```

---

## ⚙️ Installation & Requirements

The codebase is tested under the following environment. **Note:** Since this project depends on `mamba-ssm`, ensuring the consistency between PyTorch CUDA version and the system `nvcc` version is critical for successful compilation.

**Tested Environment:**
* **OS:** Linux (Ubuntu 20.04/22.04 recommended)
* **Python:** 3.10
* **CUDA Toolkit:** 12.4 (as reported by `nvcc`)
* **GPU:** NVIDIA A6000 (48GB VRAM)
* **PyTorch:** 2.2+ (compatible with CUDA 12.x)

**Installation Steps:**

We recommend using `conda` to manage the environment:

```bash
# 1. Create environment
conda create -n mambaseries python=3.10 -y
conda activate mambaseries

# 2. Install PyTorch (Ensure CUDA version matches your system nvcc)
# For CUDA 12.x:
pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cu121](https://download.pytorch.org/whl/cu121)

# 3. Install Mamba-SSM and other dependencies
# Note: 'causal-conv1d' and 'mamba-ssm' often require compilation from source.
# Ensure 'nvcc' is available in your PATH.
pip install causal-conv1d>=1.2.0
pip install mamba-ssm>=1.2.0
conda env update -f environment.yml
```

---

## 📊 Dataset Preparation

### 1. Toy Dataset (Included)

A lightweight dataset is provided in `data/ToyData/`. This allows reviewers to verify the end-to-end pipeline using the `config_toy.yaml` configuration without downloading external data.

### 2. Full Dataset

Due to size constraints, the full biological dataset is not distributed within this repository. To reproduce full experiments:

1. Place your dataset directory on your local disk.
2. Modify `exp/configs/config.yaml`:
* `data.data_dir`: Path to the dataset root.
* `data.load_name`: Metadata CSV filename (e.g., `system_info.csv`).
* `save_path_dir`: Directory for logs and checkpoints.



---

## 🚀 Quick Start (Toy Dataset)

All commands should be executed from the **repository root**.

### 1. Generative Probabilistic Forecasting
For convenience, we provide a launcher script `scripts/exp_train_FM_toy.bash` to train generative models.

**Syntax:**
```bash
bash scripts/exp_train_FM_toy.bash <max_epochs> <model_name> <gpu_id> <batch_size> <eval_freq> <seed>
Run RegimeFlow (Ours):

Bash
# Example: Train for 500 epochs on GPU 0 with seed 53
bash scripts/exp_train_FM_toy.bash 500 RegimeFlow 0 1024 50 53
Run Other Baselines: The script automatically prepends ProbabilityForecasting/ to the model name. You can simply swap the model argument:

Bash
# TSFlow with Periodic Kernel
bash scripts/exp_train_FM_toy.bash 500 TSFlow_PE 0 1024 50 53

# TSDiff / CSDI variants
bash scripts/exp_train_FM_toy.bash 500 TSDiff_regime 0 1024 50 53
bash scripts/exp_train_FM_toy.bash 500 CSDI_regime 0 1024 50 53
Note: The script handles WANDB_MODE=offline automatically. To run multiple seeds sequentially, pass them as a quoted string (e.g., "53 42 2024").
```

## 🖥️ Running on Full Dataset

To run experiments on your own data, switch to the main config file (`-cn config`) and provide the path:

```bash
WANDB_MODE=offline python exp/train_bioTFM.py \
  -cp exp/configs \
  -cn config \
  model=ProbabilityForecasting/RegimeFlow \
  data.data_dir=/path/to/full/dataset \
  data.load_name=system_info.csv \
  experiment_name=full_RegimeFlow_seed53 \
  seed=53 \
  hardware.devices=[0]

```

---

## 🧪 Evaluation

To evaluate a pre-trained model checkpoint:

```bash
WANDB_MODE=offline python exp/train_bioTFM.py \
  -cp exp/configs \
  -cn config_toy \
  model=ProbabilityForecasting/RegimeFlow \
  data.data_dir=./data/ToyData \
  data.load_name=example_info.csv \
  data.data_type=BioTFM \
  experiment_name=toy_eval \
  test_only=true \
  ckpt_path=/path/to/checkpoint.ckpt \
  hardware.devices=[0]

```

*If `training.use_ema=true` was used during training, the evaluation script will automatically load EMA weights.*

---

## 🛠️ Configuration & Hydra

This project uses [Hydra](https://hydra.cc/) for configuration.

* `-cp`: Config path (default: `exp/configs`)
* `-cn`: Config name (e.g., `config` or `config_toy`)
* Overrides: You can override any config parameter from the CLI:
* `training.max_epochs=500`
* `training.check_val_every_n_epoch=10`
* `training.limit_val_batches=1.0` (Use 100% of validation data)



---

## 🙏 Acknowledgements

We thank the authors of the following repository for their open-source contribution, which serves as the foundation for our project structure:

* **Time-Series-Library:** [https://github.com/thuml/Time-Series-Library](https://github.com/thuml/Time-Series-Library)

---

## 📄 Citation

A full citation will be provided upon publication.

```

```