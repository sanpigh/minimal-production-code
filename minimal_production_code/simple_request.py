import requests

#PORT='8080'
#url = f'http://127.0.0.1:{PORT}/multiply'

url = f'https://minimal-production-code-3jzq5a6kpq-ew.a.run.app/add'
url = f'https://minimal-production-code-3jzq5a6kpq-ew.a.run.app/dif'
#url = f'https://minimal-production-code-3jzq5a6kpq-ew.a.run.app/multiply'

       

params = {
    'a' : 14,
    'b' : 14
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())
