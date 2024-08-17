from flask import Blueprint
from src.util.obtain_response import response_obj

api = Blueprint('api', __name__)


@api.route('apiQueryset', methods=['GET'])
def get_all_api():
    api_list = [
        {'api_path': '/translate/zh-to-en', 'function': '中译英', 'method': 'get', 'query_par': 'q:string',
         'notes': '字符串长度不能大于6000字符'},
        {'api_path': '/translate/en-to-zh', 'function': '英译中', 'method': 'get', 'query_par': 'q:string',
         'notes': '字符串长度不能大于6000字符'},
        {'api_path': '/llm/dialog-chat', 'function': 'demoAI语言大模型', 'method': 'get', 'query_par': 'system:string',
         'body_par': "[{'role': 'user', 'content': '你好'}, ]:list[dic]",
         'notes': '请求体参数：对话信息，数据类型json，query参数：system模型人设'},
    ]
    return response_obj(api_list, 200)
