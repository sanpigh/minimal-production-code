import requests


url = 'http://127.0.0.1:8000/multiply'


params = {
    'a' : 2,
    'b' : 3
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())
