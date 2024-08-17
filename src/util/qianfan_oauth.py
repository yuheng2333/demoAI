
import requests
import json


def get_access_token(client_id, client_secret):
    req_url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={client_id}" \
              f"&client_secret={client_secret}"
    req_payload = ""
    req_headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", req_url, headers=req_headers, data=req_payload)
    # print(client_id, client_secret, response.text)
    return json.loads(response.text)['access_token'], json.loads(response.text)['expires_in']
