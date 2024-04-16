import json


with open('drugs.json', 'r') as jf:
    data = json.load(jf)

print(data.keys())