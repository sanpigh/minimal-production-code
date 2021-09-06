import requests

PORT='8080'
url = f'http://127.0.0.1:{PORT}/multiply'


params = {
    'a' : 2,
    'b' : 7
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())
