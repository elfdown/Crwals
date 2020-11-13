import json

with open("running.json", 'r') as f:
    cr = json.load(f)

print(len(cr))