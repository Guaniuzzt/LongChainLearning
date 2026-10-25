import os

from langchain_deepseek import ChatDeepSeek

# 当前环境只配置了 OPENAI_API_KEY，这里直接复用它作为 DeepSeek 的 Key
os.environ["DEEPSEEK_API_KEY"] = os.environ["OPENAI_API_KEY"]

# deepseek-flash 是聊天模型，用 ChatDeepSeek 访问
model = ChatDeepSeek(model="deepseek-flash")

# 通过stream方法获得流式输出
res = model.stream(input="你是谁呀能做什么？")

# 聊天模型的chunk是AIMessageChunk对象，通过.content获取文本内容
for chunk in res:
    print(chunk.content, end="", flush=True)

# 以下为其它模型的写法，可对比参考
# from langchain_community.llms.tongyi import Tongyi
#
# model = Tongyi(model="qwen-max")
#
# res = model.stream(input="你是谁呀能做什么？")
#
# for chunk in res:
#     print(chunk, end="", flush=True)
#
# from langchain_ollama import OllamaLLM
#
# model = OllamaLLM(model="qwen3:4b")
#
# res = model.stream(input="你是谁呀能做什么？")
#
# for chunk in res:
#     print(chunk, end="", flush=True)
