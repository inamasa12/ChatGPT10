import openai, json, os

openai.api_key=os.getenv('OPEN_API_KEY')

# userの条件設定
template='''
私は桃太郎であなたを仲間にしようと説得します。
鬼ヶ島へ鬼退治に行きたいのですが、仲間になってくれますか？

### 条件
- 仲間になるなら結果にtrueを、嫌ならfalseを返します。
- もしも説得内容に「きび団子」があれば{"結果": false, "理由":"食べ飽きている"}と返してください。

### 応答の例
{"結果": false, "理由": "興味がないから"}
{"結果": true, "理由": "志に共感したため"}
{"結果": false, "理由": "きび団子になんかには釣られないよ"}

###説得内容
"""__MSG__"""
'''

# ChatGPTのレスポンス取得関数
def chat_completion(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    content = response.choices[0].message.content
    return content

print('犬を見つけました。犬を仲間にしたいので説得しましょう！')

while True:
    print('---')
    # インプット取得
    msg=input(">>> ")
    # msg='きび団子をあげるから来て欲しい。'
    # msg='村の人々が困っているのを助けたい。'
    # プロンプト作成
    prompt=template.replace('__MSG__', msg.replace('"', ''))
    messages=[{'role': 'system', 'content': 'あなたは強情な犬です。JSONで応答してください。'},
              {'role': 'user', 'content': prompt}]
    # レスポンスのデフォルト設定
    res={'結果': False, '理由': '不明'}
    # レスポンスの取得
    s=chat_completion(messages)

    # レスポンス（JSON）のパース
    try:
        res=json.loads(s)
    except:
        print('[エラー] JSONの解析に失敗しました。')
    
    # 成功時の出力
    if('結果' in res) and ('理由' in res) and (res['結果']):
        print('犬は仲間になってくれました！')
        print('理由は…' + res['理由'] + '。')
        print('ゲームクリア！')
        break
    # 失敗時の出力
    else:
        reason=res['理由'] if '理由' in res else 'なし'
        print('残念。犬に断られました。理由は…' + reason + '。')
        print('引き続き説得しましょう。')


