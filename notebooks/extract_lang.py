#! /usr/bin/env python3

import sys
import json

print("Extraction en fr et en en")
for filename in sys.argv[1:]:
    print(f"    {filename}")
    for lang in ['fr', 'en']:
        with open(filename, encoding="utf-8") as f:
            data = json.loads(f.read())
            res = {}
            for k in data:
                if k == 'metadata':
                    try:
                        del data[k]['nbTranslate']
                    except:
                        pass
                    res[k] = data[k]
                elif k != 'cells':
                    res[k] = data[k]
            cells = []
            for c in data['cells']:
                try:
                    if c['metadata']['lang'] == lang:
                        cells.append(c)
                except:
                    cells.append(c)
            res['cells'] = cells
        with open(lang + '/' + filename.split('.ipynb')[0]+'.ipynb', 'w', encoding="utf-8") as outfile:
            json.dump(res, outfile, indent=1, ensure_ascii=False)
