import glob
import json
import pdb
import os

files = sorted(glob.glob('templates/*.json'))[1:-1]

data = [(fi, json.load(open(fi, 'r'))) for fi in files]
data = sorted(data, key=lambda x: x[1]['date'], reverse=True)
file_names_in_order = [os.path.basename(dd[0]) for dd in data]
json.dump(file_names_in_order, open('templates/zz_file_order.json', 'w'), indent=2)
print('Created templates index')
