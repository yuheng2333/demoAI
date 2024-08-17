from src.util.qianfan_oauth import get_access_token
import os
import qianfan
import json
import requests

# SDK
#【推荐】使用安全认证AK/SK鉴权，通过环境变量初始化认证信息
# 替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
# os.environ["QIANFAN_ACCESS_KEY"] = "xxx"
# os.environ["QIANFAN_SECRET_KEY"] = "xxx"

chat_comp = qianfan.ChatCompletion(ak="xxx", sk="xxx")

# 指定特定模型
resp = chat_comp.do(model="ERNIE-Speed-8K", messages=[{
    "role": "user",
    "content": "你好"
}])

# print(resp["body"])

# HTTP


def call_llm():
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_speed?access_token=" \
          + get_access_token("xxx", "xxx")[0]

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "介绍一下北京"
            }
        ],
        # 较高的数值会使输出更加随机，而较低的数值会使其更加集中和确定
        "temperature": 0.95,   # 范围(0, 1.0]，不能为0
        # 影响输出文本的多样性，取值越大，生成文本的多样性越强
        "top_p": 0.7,   # 范围[0, 1.0]
        # 通过对已生成的token增加惩罚，减少重复生成的现象，取值越大惩罚越大
        "penalty_score": 1.0,  # 范围[1.0, 2.0]
        # 模型人设，主要用于人设设定，例如：你是xxx公司制作的AI助手
        "system": '',
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

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


if __name__ == "__main__":
    call_llm()
