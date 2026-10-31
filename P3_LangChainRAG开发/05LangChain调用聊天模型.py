import os

from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 当前环境只配置了 OPENAI_API_KEY，这里直接复用它作为 DeepSeek 的 Key
os.environ["DEEPSEEK_API_KEY"] = os.environ["OPENAI_API_KEY"]

# 得到模型对象, deepseek-flash就是聊天模型
model = ChatDeepSeek(model="deepseek-flash")

# 准备消息列表
messages = [
    SystemMessage(content="你是一个边塞诗人。"),
    HumanMessage(content="写一首唐诗"),
    AIMessage(content="锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。"),
    HumanMessage(content="按照你上一个回复的格式，在写一首唐诗。")
]

# 调用stream流式执行
res = model.stream(input=messages)

# for循环迭代打印输出，通过.content来获取到内容
for chunk in res:
    print(chunk.content, end="", flush=True)
