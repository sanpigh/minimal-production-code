import requests

PORT='8080'
url = f'http://127.0.0.1:{PORT}/multiply'

url = f'https://minimal-production-code-docker-image-gcp-3jzq5a6kpq-ew.a.run.app/multiply'

params = {
    'a' : 13,
    'b' : 13
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())
