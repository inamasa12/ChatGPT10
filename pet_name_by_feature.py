import openai, os

openai.api_key = os.environ["OPEN_API_KEY"]

def call_chatgpt(prompt, debug=False):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user', 'content': prompt}]
    )
    
    if debug: print(response)

    content = response.choices[0]['message']['content']
    return content

# features = input('ペットの特徴を入力してください: ')
features = 'フレンチブルドッグ'

if features == '': quit()

prompt = f"""
ペットの名前を3つ考えてください。
特徴: '''{features}'''
"""

pet_names = call_chatgpt(prompt, debug=False)

print(pet_names)
