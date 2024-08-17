from flask import Blueprint, current_app
from flask import request
from src.util.obtain_response import response_obj
from src.util.call_texttrans import get_trans_res
from src.util.qianfan_oauth import get_access_token

import re
import json

translate = Blueprint('translate', __name__)


@translate.route('/zh-to-en', methods=['GET'])
def zh_to_en():
    req_data = request.args.get('q')
    if len(req_data) > 6000:
        return response_obj({'err_msg': '长度不能大于6000'}, 406)
    url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + get_access_token(current_app.config["TRANSLATE_AK"], current_app.config["TRANSLATE_SK"])[0]
    from_lang = 'zh'
    to_lang = 'en'
    res = get_trans_res(url, req_data, from_lang, to_lang)
    if json.loads(res).get('error_msg'):
        return response_obj({'error_msg': res.get('error_msg')}, 500)
    return response_obj(res['result'], 200)


@translate.route('/en-to-zh', methods=['GET'])
def en_to_zh():
    q = request.args.get('q')
    if len(q) > 6000:
        return response_obj({'err_msg': '长度不能大于6000'}, 406)
    url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + get_access_token(current_app.config["TRANSLATE_AK"], current_app.config["TRANSLATE_SK"])[0]
    from_lang = 'en'
    to_lang = 'zh'
    res = get_trans_res(url, q, from_lang, to_lang)
    if json.loads(res).get('error_msg'):
        return response_obj({'error_msg': res.get('error_msg')}, 500)
    return response_obj(res['result'], 200)
