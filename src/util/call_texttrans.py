import requests


def get_trans_res(url, q, before, to):
    headers = {'Content-Type': 'application/json'}
    payload = {'q': q, 'from': before, 'to': to, 'termIds': ''}
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    return result
