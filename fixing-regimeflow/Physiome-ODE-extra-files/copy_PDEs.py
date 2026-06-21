import pandas as pd
import shutil
from pathlib import Path
from tqdm import tqdm

# -------- CONFIG --------
csv_path = "CellML_model_list_updates.csv"
destination_root = Path("Physiome-PDE")  # change as needed
destination_root.mkdir(parents=True, exist_ok=True)

# -------- LOAD CSV --------
df = pd.read_csv(csv_path)

# Ensure correct column name (strip whitespace just in case)
df.columns = df.columns.str.strip()

# -------- FILTER PDE MODELS --------
pde_df = df[df["PDE count"] > 0]

print(f"Found {len(pde_df)} PDE models")

# -------- COPY FILES --------
success = 0
fail = 0

for _, row in tqdm(pde_df.iterrows(), total=len(pde_df)):
    src_path = Path(row["File"])
    model_name = row["Model Name"]

    try:
        if not src_path.exists():
            print(f"[MISSING] {src_path}")
            fail += 1
            continue

        # Optional: organize by model name
        dest_dir = destination_root# / model_name
        dest_dir.mkdir(parents=True, exist_ok=True)

        dest_path = dest_dir / src_path.name

        # Avoid overwrite collisions
        if dest_path.exists():
            base = dest_path.stem
            suffix = dest_path.suffix
            i = 1
            while (dest_dir / f"{base}_{i}{suffix}").exists():
                i += 1
            dest_path = dest_dir / f"{base}_{i}{suffix}"

        shutil.copy2(src_path, dest_path)
        success += 1

    except Exception as e:
        print(f"[ERROR] {src_path}: {e}")
        fail += 1

# -------- SUMMARY --------
print("\nDone.")
print(f"Success: {success}")
print(f"Failed: {fail}")