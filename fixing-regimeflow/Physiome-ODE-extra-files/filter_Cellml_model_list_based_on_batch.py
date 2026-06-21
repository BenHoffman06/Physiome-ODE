import pandas as pd
import os

# Load
df_status = pd.read_csv("wrapped_models/batch_run_results.csv")
df_models = pd.read_csv("CellML_model_list_only_ODE.csv")

# ----------------------------
# Extract Model Name
# ----------------------------
df_status["Model Name"] = (
    df_status["wrapped_model_file"]
    .apply(lambda x: os.path.basename(x).replace("_wrapped.py", ""))
)

# ----------------------------
# Filter OK
# ----------------------------
df_ok = df_status[df_status["status"] == "ok"]

# ---- Count check 1 ----
n_ok_status = len(df_ok)
print(f"OK rows in status.csv: {n_ok_status}")

# ----------------------------
# Filter models.csv
# ----------------------------
filtered_models = df_models[
    df_models["Model Name"].isin(df_ok["Model Name"])
]

# ---- Count check 2 ----
n_filtered = len(filtered_models)
print(f"Matched models in models.csv: {n_filtered}")

# ----------------------------
# Debug mismatch (important)
# ----------------------------
missing = set(df_ok["Model Name"]) - set(df_models["Model Name"])
print(f"OK models NOT found in models.csv: {len(missing)}")

# Optional: print a few if something is off
if missing:
    print(list(missing)[:10])

# ----------------------------
# Save
# ----------------------------
filtered_models.to_csv("filtered_models_ok.csv", index=False)