from flask import Blueprint, current_app
from flask import request
from src.util.qianfan_oauth import get_access_token
from src.util.obtain_response import response_obj

import json
import requests

llm = Blueprint('llm', __name__)


@llm.route('dialog-chat', methods=['GET'])
def dialog_chat():
    all_role = ['user', 'assistant']
    try:
        chat_query = json.loads(request.data)
    except json.JSONDecodeError:
        return response_obj({'error_msg': '请求体数据类型错误，请检查请求体是否传入的是json数据'}, 406)
    model_design = request.args.get('system', '')
    for i, val in enumerate(chat_query):
        role = chat_query[i].get('role', None)
        content = chat_query[i].get('content', None)
        if not content or (role not in all_role):
            return response_obj({'error_msg': '请求体数据有误，请检查后重试'}, 406)
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_speed?access_token=" \
          + get_access_token(current_app.config["LLM_AK"], current_app.config["LLM_SK"])[0]
    payload = json.dumps({
        "messages": chat_query,
        # 较高的数值会使输出更加随机，而较低的数值会使其更加集中和确定
        "temperature": 0.95,  # 范围(0, 1.0]，不能为0
        # 影响输出文本的多样性，取值越大，生成文本的多样性越强
        "top_p": 0.7,  # 范围[0, 1.0]
        # 通过对已生成的token增加惩罚，减少重复生成的现象，取值越大惩罚越大
        "penalty_score": 1.0,  # 范围[1.0, 2.0]
        # 模型人设，主要用于人设设定，例如：你是xxx公司制作的AI助手
        "system": model_design,
        # 声称停止标志，当模型结果以stop中某个元素结尾时，停止生成文本
        "stop": [],
        # 指定模型最小输出token数，说明：该参数取值范围[2, 2048]
        "min_output_tokens": 2,
        #  指定模型最大输出token数，如果设置此参数，范围[2, 2048],如果不设置此参数，最大输出token数为1024
        "max_output_tokens": 1024
    })
    headers = {
        'Content-Type': 'application/json'
    }

    res = requests.request("POST", url, headers=headers, data=payload)
    if json.loads(res.text).get('error_msg'):
        return response_obj({'error_code': 110, 'error_msg': json.loads(res.text)['error_msg']}, 500)
    return response_obj(res.text, 200)
