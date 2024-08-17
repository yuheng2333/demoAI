import os


class Config:
    BASE_DIR = os.getcwd()
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    DEBUG = False
    # translate ak sk
    TRANSLATE_AK = "your translate ak"
    TRANSLATE_SK = "your translate sk"
    # LLM ak sk
    LLM_AK = "your llm ak"
    LLM_SK = "your llm sk"


config = Config()
PORT = 8000
ADDRESS = '127.0.0.1'
