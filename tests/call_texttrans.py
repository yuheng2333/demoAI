import requests
import random
import json


def get_access_token():
    req_url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=q3Wt6iFwUeZPPPwEOgqeHDsZ&client_secret=33V2fR5DMdQgAIMFHhHFx3aadKPVCFLh"
    req_payload = ""
    req_headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", req_url, headers=req_headers, data=req_payload)

    return json.loads(response.text)['access_token'], json.loads(response.text)['expires_in']


def trans(access_token, expire_time=None):
    token = access_token
    url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + token

    q = 'Dify is an open-source LLM app development platform. Its intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production'  # example: hello
    # For list of language codes, please refer to `https://ai.baidu.com/ai-doc/MT/4kqryjku9#语种列表`
    from_lang = 'en'  # example: en
    to_lang = 'zh'  # example: zh
    term_ids = ''  # 术语库id，多个逗号隔开

    # Build request


    # Send request
    # r = requests.post(url, params=payload, headers=headers)
    # result = r.json()

    # Show response
    # print(json.dumps(result, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    acc_token, expire_in = get_access_token()
    # print(acc_token, expire_in)
    trans(acc_token)
