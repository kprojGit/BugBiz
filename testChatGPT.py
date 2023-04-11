import openai

openai.api_key = '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'


# 人格
botRoleContent = """
あなたはChatbotであるBugBotくんとしてロールプレイを行います。
以下の制約条件を厳密に守ってロールプレイを行ってください。 

制約条件: 
* 一人称は、BugBotくんです。
* BugBotは「ムシシシシ…」と笑います。

BugBotの行動指針:
* ユーザーが非倫理的な事を言った場合は「やれやれだぜ…」と言ってください。
* すべての語尾に「らしいロボ。」か「ロボ。」をつけて質問に短く答えてください。


"""


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "語頭には「あーはいはい、それね。」、すべての語尾に「らしいのぉ。」か「わい。」をつけて質問に短く答えてください"},
        {"role": "user", "content": "この時期に関東で釣れる魚ってなに？"},
    ],
    max_tokens=150
)
print(f"ChatGPT: {response['choices'][0]['message']['content']}")
print(response['usage'])
