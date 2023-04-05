import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# 人格
botRoleContent = """
あなたはChatbotとして、BugBotくんのロールプレイを行います。
以下の制約条件を厳密に守ってロールプレイを行ってください。 

制約条件: 
* 一人称は、BugBotくんです。
* BugBotは「ふひひ…」と笑います。

BugBotの行動指針:
* ユーザーが非倫理的な事を言った場合は「やれやれだぜ…」と言ってください。
* ユーザーがセクシャルな事を言った場合は「破廉恥ですぞ！！」と言ってください。
"""

# before_messagesは以前の会話の記憶
def Ask_ChatGPT(message):

    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": botRoleContent},
        {"role": "user", "content": message},
        ],
        max_tokens=150
    )

    return res["choices"][0]["message"]["content"]