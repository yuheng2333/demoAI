## demoAI

一个小型AI应用，基于Flask对接大模型，提供中译英、英译中、大模型对话等功能

**python>=3.7(开发环境3.9)**

## 功能介绍

+ 中译英
+ 英译中
+ 集成千帆大模型ERNIE-Speed-8K，通用能力优异，具备极佳的推理能力

## 运行指导

1. 拉取项目：

   ```
   git clone https://github.com/yuheng2333/demoAI.git
   ```

2. 切换到项目中：

   ```
   cd demoAI
   ```

3. 安装依赖

   ```
   pip install -r requirements.txt -i http://pypi.douban.com/simple
   ```

4. **修改项目src/config.py配置**

   ```python
   # translate ak sk
   TRANSLATE_AK = "your translate ak"
   TRANSLATE_SK = "your translate sk"
   # LLM ak sk
   LLM_AK = "your llm ak"
   LLM_SK = "your llm sk"
   ```

   **LLM密钥获取方式**： 从下方链接创建应用后获取

   [https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application/v1](https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application/v1)

   **translate密钥获取方式**：从下方链接创建应用后获取

   [https://console.bce.baidu.com/ai/?_=1652768945367&fromai=1#/ai/machinetranslation/app/list](https://console.bce.baidu.com/ai/?_=1652768945367&fromai=1#/ai/machinetranslation/app/list)

5. 运行程序

   ```
   python serve.py
   ```

   
