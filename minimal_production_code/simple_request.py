import requests

#PORT='8080'
#url = f'http://127.0.0.1:{PORT}/multiply'

#url = f'https://minimal-production-code-3jzq5a6kpq-ew.a.run.app/add'
#url = f'https://minimal-production-code-3jzq5a6kpq-ew.a.run.app/dif'
#url = f'https://minimal-production-code-3jzq5a6kpq-ew.a.run.app/multiply'


def get_sum(a, b):
    url = f'https://minimal-production-code-3jzq5a6kpq-ew.a.run.app/add'
    params = {
        'a' : a,
        'b' : b
    }
    response = requests.get(url, params=params)
    return response.status_code, response.json()['a+b'] 


if __name__ == '__main__':
    status, addition = get_sum(1, 2)
    print(status, addition)
