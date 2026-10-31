import os

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_deepseek import ChatDeepSeek

# 当前环境只配置了 OpenAI 的 key，这里直接复用它作为 DeepSeek 的 Key
os.environ["DEEPSEEK_API_KEY"] = os.environ["OPENAI_API_KEY"]

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个边塞诗人，可以作诗。"),
        MessagesPlaceholder("history"),
        ("human", "请再来一首唐诗"),
    ]
)

history_data = [
    ("human", "你来写一个唐诗"),
    ("ai", "床前明月光，疑是地上霜，举头望明月，低头思故乡"),
    ("human", "好诗再来一个"),
    ("ai", "锄禾日当午，汗滴禾下锄，谁知盘中餐，粒粒皆辛苦"),
]

model = ChatDeepSeek(model="deepseek-flash")

# 组成链，要求每一个组件都是Runnable接口的子类
chain = chat_prompt_template | model

# 通过链去调用invoke或stream
# res = chain.invoke({"history": history_data})
# print(res.content)

# 通过stream流式输出
for chunk in chain.stream({"history": history_data}):
    print(chunk.content, end="", flush=True)
