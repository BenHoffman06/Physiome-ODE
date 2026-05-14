# RegimeFlow

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Framework](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![Conference](https://img.shields.io/badge/ICML-2026%20Accepted-green)](https://icml.cc/)
[![Paper](https://img.shields.io/badge/Paper-OpenReview-blue)](https://openreview.net/forum?id=sI3UUkXJxs)
[![Dataset](https://img.shields.io/badge/Dataset-Hugging%20Face-yellow)](https://huggingface.co/datasets/HengRao/SysBio-Traj)

**RegimeFlow** is a regime-aware flow matching framework for probabilistic
forecasting of biological trajectories across dynamical systems.

This repository is the official implementation of
**A Regime-Aware Trajectory Prediction Framework for 1000+ Systems Biology
Models**, accepted to **ICML 2026**.

## Quick Links

| I want to... | Go to |
|---|---|
| Install the environment | [Installation](#installation) |
| Download and place the dataset | [Dataset and Paths](#dataset-and-paths) |
| Run RegimeFlow quickly | [Run with Scripts](#run-with-scripts) |
| Evaluate a checkpoint | [Evaluation](#evaluation) |
| Run point-forecasting baselines | [Point Forecasting Note](#point-forecasting-note) |
| Use Chronos | [Chronos Baseline](#chronos-baseline) |
| See all model names | [Supported Models](#supported-models) |

## What This Repo Provides

| Component | Description |
|---|---|
| RegimeFlow | Regime-aware probabilistic trajectory forecasting model |
| Probabilistic baselines | TSFlow and diffusion-based forecasting baselines |
| Point baselines | iTransformer, PatchTST, DLinear, S-Mamba, BiMamba4TS, TimeMixer, TimeXer, NSformer, Chronos |
| Dataset support | Loader for the released SysBio-Traj benchmark |
| Reproduction scripts | Bash launchers for common full-dataset experiments |

> [!TIP]
> If you are using this repository for the first time, follow this order:
> install the environment, download SysBio-Traj, edit `exp/configs/config.yaml`,
> then run the bash scripts in `scripts/`.

---

## Installation

The project has been tested with the following setup.

| Dependency | Tested version |
|---|---|
| OS | Ubuntu 22.04+ |
| Python | 3.10.19 |
| PyTorch | 2.9.1 |
| CUDA toolkit (`nvcc`) | 12.4 |
| GPU | NVIDIA RTX A6000 |
| `mamba-ssm` | 2.2.6 |

Create the conda environment:

```bash
conda env create -f environment.yml
conda activate mambaseries
```

> [!WARNING]
> This repository depends on `mamba-ssm` v2.x. If your local CUDA compiler is
> incompatible with the CUDA version used by PyTorch, you may see ABI or
> `undefined symbol` errors.

If `mamba-ssm` fails to import, rebuild the low-level dependencies from source:

```bash
pip install "causal-conv1d>=1.4.0" --no-binary causal-conv1d --force-reinstall --no-cache-dir
pip install "mamba-ssm>=2.2.6" --no-binary mamba-ssm --force-reinstall --no-cache-dir
```

Before rebuilding, check that `nvcc --version` is available and compatible with
your PyTorch build.

---

## Dataset and Paths

The full biological trajectory dataset is available on Hugging Face:

```text
https://huggingface.co/datasets/HengRao/SysBio-Traj
```

Download it locally:

```bash
huggingface-cli download HengRao/SysBio-Traj \
  --repo-type dataset \
  --local-dir /path/to/SysBio-Traj
```

Expected dataset layout:

```text
/path/to/SysBio-Traj/
├── SysBio-Traj_index.csv
└── Data/
    └── <model_id>/
        ├── <model_name>.csv
        └── <model_name>_conditions.json
```

> [!IMPORTANT]
> `SysBio-Traj_index.csv` must contain at least `model_id` and `model_name`.
> The loader builds each trajectory path as
> `<data.data_dir>/Data/<model_id>/<model_name>.csv`.

Edit the main config before running experiments:

```yaml
# exp/configs/config.yaml
save_path_dir: /path/to/outputs

data:
  data_dir: /path/to/SysBio-Traj
  load_name: SysBio-Traj_index.csv

hardware:
  devices: [0]
```

| Field | Meaning |
|---|---|
| `data.data_dir` | Root directory of the downloaded SysBio-Traj dataset |
| `data.load_name` | Metadata CSV filename under `data.data_dir` |
| `save_path_dir` | Output root for checkpoints, logs, predictions, and Hydra outputs |
| `hardware.devices` | GPU index list used by PyTorch Lightning |

> [!IMPORTANT]
> The bash launchers read `data.data_dir` from `exp/configs/config.yaml`.
> They currently assume `load_name="SysBio-Traj_index.csv"` near the top of
> each script. If you rename the metadata file, update the script as well.

---

## Run with Scripts

The scripts are the fastest path for reproducing common full-dataset runs.

> [!NOTE]
> All commands in this README assume you are running from the repository root.

### RegimeFlow

```bash
bash scripts/exp_train_FM.bash 500 RegimeFlow 0 1024 50 "53"
```

### Probabilistic Baselines

```bash
bash scripts/exp_train_FM.bash 500 TSFlow_PE 0 1024 50 "53"
bash scripts/exp_train_FM.bash 500 TSDiff_regime 0 1024 50 "53"
bash scripts/exp_train_FM.bash 500 CSDI_regime 0 1024 50 "53"
```

### Point Forecasting Baselines

```bash
bash scripts/exp_train_Point.bash 100 iTransformer 0 64 10 "53"
```

### Chronos Zero-Shot Evaluation

```bash
bash scripts/exp_train_Point_chronos.bash 1 Chronos 0 64 1 "53" /path/to/local/chronos-checkpoint
```

Script signatures:

```text
exp_train_FM.bash <max_epochs> <model_name> <gpu_id> <batch_size> <eval_freq> "<seeds>"
exp_train_Point.bash <max_epochs> <model_name> <gpu_id> <batch_size> <eval_freq> "<seeds>"
exp_train_Point_chronos.bash <max_epochs> <model_name> <gpu_id> <batch_size> <eval_freq> "<seeds>" <local_model_dir> [offline_mode]
```

> [!TIP]
> For multiple seeds, pass a quoted space-separated list, for example
> `"53 25 81"`.

---

## Run with Hydra

Use direct Hydra commands when you want all paths and overrides visible in the
command line.

```bash
WANDB_MODE=offline python exp/train_bioTFM.py \
  -cp ./configs \
  -cn config \
  model=ProbabilityForecasting/RegimeFlow \
  data.data_dir=/path/to/SysBio-Traj \
  data.load_name=SysBio-Traj_index.csv \
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

Switch models by changing only the `model=` override when staying within the
same model family:

```bash
model=ProbabilityForecasting/RegimeFlow
model=ProbabilityForecasting/TSFlow_PE
model=ProbabilityForecasting/TSDiff_regime
model=ProbabilityForecasting/CSDI_regime
```

### Point Forecasting Note

> [!IMPORTANT]
> Every `PointForecasting/*` model must use `data.data_type=PointTrajectory`
> and `training.use_ema=false`. The bash scripts already set these values.
> Add them manually when using Hydra directly.

```bash
WANDB_MODE=offline python exp/train_bioTFM.py \
  -cp ./configs \
  -cn config \
  model=PointForecasting/iTransformer \
  data.data_dir=/path/to/SysBio-Traj \
  data.load_name=SysBio-Traj_index.csv \
  data.data_type=PointTrajectory \
  training.use_ema=false \
  save_path_dir=/path/to/outputs \
  experiment_name=full_iTransformer_seed53 \
  seed=53 \
  training.max_epochs=100 \
  data.batch_size=64 \
  hardware.devices=[0]
```

---

## Evaluation

Evaluate a probabilistic checkpoint:

```bash
WANDB_MODE=offline python exp/train_bioTFM.py \
  -cp ./configs \
  -cn config \
  model=ProbabilityForecasting/RegimeFlow \
  data.data_dir=/path/to/SysBio-Traj \
  data.load_name=SysBio-Traj_index.csv \
  data.data_type=BioTFM \
  save_path_dir=/path/to/outputs \
  experiment_name=full_RegimeFlow_eval \
  test_only=true \
  ckpt_path=/path/to/checkpoint.ckpt \
  hardware.devices=[0]
```

> [!NOTE]
> If a checkpoint contains `ema_state_dict`, the evaluation script
> automatically uses EMA weights.

Evaluate a point-forecasting checkpoint:

```bash
WANDB_MODE=offline python exp/train_bioTFM.py \
  -cp ./configs \
  -cn config \
  model=PointForecasting/iTransformer \
  data.data_dir=/path/to/SysBio-Traj \
  data.load_name=SysBio-Traj_index.csv \
  data.data_type=PointTrajectory \
  training.use_ema=false \
  save_path_dir=/path/to/outputs \
  experiment_name=full_iTransformer_eval \
  test_only=true \
  ckpt_path=/path/to/checkpoint.ckpt \
  hardware.devices=[0]
```

> [!WARNING]
> For `PointForecasting/*` evaluation, always set `training.use_ema=false`.
> Leaving the default EMA setting enabled can cause evaluation errors.

---

## Chronos Baseline

Chronos is integrated through the point-forecasting pipeline and is currently
used for zero-shot evaluation.

The default Chronos config uses **Chronos-Bolt Base**:

```text
https://huggingface.co/amazon/chronos-bolt-base
```

Download it locally:

```bash
huggingface-cli download amazon/chronos-bolt-base \
  --local-dir /path/to/local/chronos-checkpoint
```

The local checkpoint directory should contain:

- `config.json`
- `model.safetensors`

Run Chronos:

```bash
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 WANDB_MODE=offline python exp/train_bioTFM.py \
  -cp ./configs \
  -cn config \
  model=PointForecasting/Chronos \
  data.data_dir=/path/to/SysBio-Traj \
  data.load_name=SysBio-Traj_index.csv \
  data.data_type=PointTrajectory \
  training.use_ema=false \
  save_path_dir=/path/to/outputs \
  experiment_name=full_Chronos \
  seed=53 \
  test_only=true \
  test_without_ckpt=true \
  data.batch_size=64 \
  hardware.devices=[0] \
  model.model.args.pretrained_model_path=/path/to/local/chronos-checkpoint \
  model.model.args.local_files_only=true \
  model.model.args.device_map=cuda:0
```

> [!IMPORTANT]
> For Chronos on a non-zero GPU, keep `hardware.devices` and
> `model.model.args.device_map` aligned, for example
> `hardware.devices=[2] model.model.args.device_map=cuda:2`. The
> `scripts/exp_train_Point_chronos.bash` launcher sets this automatically from
> its `<gpu_id>` argument.

---

## Supported Models

| Family | Config names |
|---|---|
| Probabilistic forecasting | `RegimeFlow`, `TSFlow_PE`, `TSFlow_PE_regime`, `TSDiff_regime`, `CSDI_regime` |
| Point forecasting | `iTransformer`, `PatchTST`, `DLinear`, `S_Mamba`, `BiMamba4TS`, `TimeMixer`, `TimeXer`, `NSformer`, `Chronos` |

Use the full config path when launching:

```bash
model=ProbabilityForecasting/RegimeFlow
model=PointForecasting/iTransformer
```

Model configs are located under:

- `exp/configs/model/ProbabilityForecasting/`
- `exp/configs/model/PointForecasting/`

---

## Hydra Notes

| Flag / override | Meaning |
|---|---|
| `-cp ./configs` | Config directory, resolved relative to `exp/train_bioTFM.py` |
| `-cn config` | Main full-dataset config |
| `data.data_dir=...` | Dataset root |
| `data.load_name=...` | Metadata CSV filename |
| `save_path_dir=...` | Output root |
| `hardware.devices=[0]` | GPU list |

Common overrides:

```bash
data.data_dir=/path/to/SysBio-Traj
data.load_name=SysBio-Traj_index.csv
save_path_dir=/path/to/outputs
training.max_epochs=500
training.check_val_every_n_epoch=10
data.batch_size=1024
hardware.devices=[0]
```

> [!IMPORTANT]
> `training.use_ema=false` is required for `PointForecasting/*` models, but
> should generally remain enabled for RegimeFlow and other probabilistic runs
> unless you intentionally disable EMA.

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

<details>
<summary>Repository map</summary>

```text
.
├── dataset/                      # Dataset loading, filtering, and splits
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
└── Materials/                    # Optional pretrained assets and references
```

</details>

---

## Acknowledgements

We thank the authors of
**[Time-Series-Library](https://github.com/thuml/Time-Series-Library)** for
their open-source contribution, which serves as the basis of our
training/evaluation infrastructure.

---

## Citation

If you find this repository useful, please cite the ICML 2026 paper:

```bibtex
@inproceedings{rao2026regime,
  title     = {A Regime-Aware Trajectory Prediction Framework for 1000+ Systems Biology Models},
  author    = {Rao, Heng and Zhang, Jason Zipeng and Gu, Yu and Liu, Zhenghao and Yu, Ge and Su, Jeffrey and Cao, Yang and Yang, Fan and Chen, Minghan},
  booktitle = {Proceedings of the 43rd International Conference on Machine Learning},
  year      = {2026},
  url       = {https://openreview.net/forum?id=sI3UUkXJxs}
}
```
