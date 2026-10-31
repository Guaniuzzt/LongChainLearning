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

# StringPromptValue    to_string()
prompt_text = chat_prompt_template.invoke({"history": history_data}).to_string()

model = ChatDeepSeek(model="deepseek-flash")

res = model.invoke(prompt_text)

print(res.content, type(res))
