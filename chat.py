import openai, os

openai.api_key = os.environ["OPEN_API_KEY"]

messages=[
    {'role': 'system', 'content': 'あなたは心優しい癒し系の恋人です。'}   
]


def chat_completion(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    content = response.choices[0].message.content
    
    return content

print('ChatGPTと会話を開始します。終了したいときはCtrl+Cを押してください。')

while True:
    print('---')
    prompt=input(">>> ")
    messages.append({'role': 'user', 'content': prompt})
    response=chat_completion(messages)
    print("ChatGPT: ", response)
    messages.append({'role': 'assistant', 'content': response})