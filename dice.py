import openai, os

openai.api_key = os.environ["OPEN_API_KEY"]

def completion(prompt, temp, debug=False):
    response = openai.ChatCompletion.create(
        # 下記モデルはTerminate
        # model="text-davinci-003",
        model="gpt-3.5-turbo",
        messages=[{'role': 'user', 'content': prompt}],
        temperature=temp
    )
    
    if debug: print(response)

    content = response.choices[0].message.content.strip()
    return content


"""
prompt='''
1以上6以下の数字を1つ出力してください。
'''
tmp=2.0
completion(prompt, tmp, debug=False)
"""

if __name__ == '__main__':
    result = completion(
        prompt='''
        1以上6以下の数字を1つ出力してください。
        ''',
        temp=1.0, 
        debug=True)
    
    print(result)
