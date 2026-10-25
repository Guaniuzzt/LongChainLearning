import os

from langchain_deepseek import ChatDeepSeek

# 当前环境只配置了 OPENAI_API_KEY，这里直接复用它作为 DeepSeek 的 Key
# 等价于命令行里的 DEEPSEEK_API_KEY="$OPENAI_API_KEY"
os.environ["DEEPSEEK_API_KEY"] = os.environ["OPENAI_API_KEY"]

# deepseek-flash 是聊天模型，用 ChatDeepSeek 访问（需要先 pip install langchain-deepseek）
# API Key 从环境变量 DEEPSEEK_API_KEY 读取，也可以显式传 api_key="sk-xxx"
model = ChatDeepSeek(model="deepseek-flash")

# 调用invoke向模型提问
res = model.invoke(input="你是谁呀能做什么？")

# 聊天模型返回的是AIMessage对象，通过content获取文本内容
print(res.content)
