import requests

PORT='8000'
url = f'http://127.0.0.1:{PORT}/prediction'

#url = f'https://minimal-production-code-3jzq5a6kpq-ew.a.run.app/add'
#url = f'https://minimal-production-code-3jzq5a6kpq-ew.a.run.app/dif'
#url = f'https://minimal-production-code-3jzq5a6kpq-ew.a.run.app/multiply'
#url = f'https://minimal-production-code-3jzq5a6kpq-ew.a.run.app/prediction'

       

params = {
    'a' : 14,
    'b' : 14
}

#response = requests.get(url, params=params)
response = requests.get(url)
print('outside')
print(response.status_code)
print('outside2')

print(response.json())
print('outside3')
