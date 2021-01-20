import requests


def get_valores():
    resp = requests.get('https://api.exchangeratesapi.io/history?start_at=2020-12-29&end_at=2021-01-05&symbols=USD')
    if resp.status_code != 200:
        print('Error code'.format(resp.status_code))
    return resp.json()['rates']
