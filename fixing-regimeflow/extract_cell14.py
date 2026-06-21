import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\Benem\Downloads\Regime-Flow-AI\fixing-regimeflow\my_changed_files\run_pipeline-i-ran.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

source = ''.join(nb['cells'][14]['source'])
print(source)
