# Wrapped CellML Models

## Folder Structure

run_all_wrapped_models.py

wrapped_models/
    └── {domain}/
        └── {model}/
            ├── model.cellml             # CellML model definition
            ├── model_wrapped.py        # Python wrapper used for simulation
            ├── model_conditions.json   # Default initial conditions + parameters
            └── model.csv               # Output trajectory (generated)

---

## File Roles

- run_all_wrapped_models.py
  - Batch runner
  - Finds all models under wrapped_models/
  - Runs simulations
  - Writes model.csv in each model folder
  - Tracks successes and failures

- model.cellml
  - Source model definition

- model_wrapped.py
  - Executable version of the model (used by runner)

- model_conditions.json
  - Initial values + editable parameters
  - Used to initialize simulation

- model.csv
  - Output trajectory
  - Format:
    t,var1,var2,...

---

## Running

Default run (1000 steps):
python run_all_wrapped_models.py

Custom number of steps:
python run_all_wrapped_models.py --steps N

Optional: use custom conditions (per model):
- Place {model}.json in the model directory
- Runner will use it instead of model_conditions.json

---

## Notes

- Each model is self-contained in its folder
- Output is written in-place (model.csv)
- Assumes ODE models only
- Failures are logged and counted by the runner