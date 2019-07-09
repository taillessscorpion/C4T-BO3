import json
with open('data_text.json') as f:
    d = json.load(f)
r = json.dumps(d)
print (d)