import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'my_changed_files/run_pipeline-i-ran.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        outputs = cell.get('outputs', [])
        for out in outputs:
            text = ""
            if 'text' in out:
                text = ''.join(out['text'])
            elif 'data' in out and 'text/plain' in out['data']:
                text = ''.join(out['data']['text/plain'])
            if text.strip():
                print(f'--- Cell {i} Output ---')
                print(text)
                print()
