import openai, json, os

openai.api_key=os.getenv('OPEN_API_KEY')

# userの条件設定
template='''
次の題の文章について、論理的かどうか、ユニークかどうかを0から100で採点してください。

### 題
- 桃太郎が鬼退治に行く仲間を探す

### 応答の例
{"論理":80, "ユニーク": 30, "論評": "論理的だが、ありふれた内容で、心が動かない"}
{"論理":50, "ユニーク": 90, "論評": "論理的ではないが、ユニークで面白い"}

### 文章
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

point=0

print('犬を見つけました。犬を仲間にしたいので説得しましょう！')

while True:
    # インプット取得
    msg=input(">>> ")
    # msg='きび団子をあげるから来て欲しい。'
    # msg='村の人々が困っているのを助けたい。'
    # プロンプト作成
    prompt=template.replace('__MSG__', msg.replace('"', ''))
    messages=[{'role': 'system', 'content': 'JSONで応答してください。'},
              {'role': 'user', 'content': prompt}]
    # レスポンスの取得
    s=chat_completion(messages)

    # レスポンス（JSON）のパース
    try:
        logic, unique, comment=0, 0, '?'
        res=json.loads(s)
        if '論理' in res: logic=res['論理']
        if 'ユニーク' in res: unique=res['ユニーク']
        if '論評' in res: comment=res['論評']
        point += logic + unique
    except:
        print('[エラー] JSONの解析に失敗しました。', s)
        continue
    
    # 結果の出力
    print(f'論理: {logic}点、ユニーク: {unique}点 → {comment}')
    print(f'--- 合計得点: {point} ---')

    # 300点以上で成功
    if point>=300:
        print('犬が仲間になってくれました！')
        print('ゲームクリア！')
        break
    # 失敗
    else:
        print('引き続き説得しましょう。')

