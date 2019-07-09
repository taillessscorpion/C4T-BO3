import requests
import json
payload = {'username': 'Delphine'}
r = requests.get('https://jsonplaceholder.typicode.com/users', params = payload)

d = json.loads(r.text)
with open('data_text.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=5)
