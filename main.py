# 自然言語で操作するToDOアプリ
import openai, json, time
import todo_functions
import actions

# ChatGPTを呼び出すためのメッセージを構築 --- (*1)
# プロンプト
messages = [{
    'role': 'system',  # システムの役割を指定
    'content': 'あなたはタスク管理の優秀なエージェントです。'
}]

# プロンプトに関数に入力するテキスト文を加える（ここがポイント）
# order_text = 'プロジェクトAの予算案の作成をタスクに追加して。'
# order_text = '最新の3件のタスクを見せて。'
# order_text = '5を完了'
# order_text = '4番を削除して。'
# order_text = '加藤さんとの打ち合わせの日程をメールで話し合うことをタスクに入れて。'
# messages.append({'role': 'user', 'content': order_text})

# ToDOアイテムを保持する --- (*2)
# 独自モジュール
# 全てのタスクを表示し、リストとして読み込む
todo_items = actions.load_items()

# ToDOボットを実行する --- (*3)
def call_todo_bot(messages, functions=None, debug=False):
    # 希にAPI呼び出しが失敗するので自動的にリトライ --- (*4)
    # debug=False
    while True:
        try:
            # APIの呼び出し --- (*5)
            # Function Calling
            model = 'gpt-3.5-turbo-0613'
            if functions is not None:  # 関数の指定があるとき
                response = openai.ChatCompletion.create(
                    model=model, messages=messages,
                    functions=functions,
                    function_call='auto')
            # シンプルなプロンプトのやりとり
            else:  # 関数の指定がなかったとき
                response = openai.ChatCompletion.create(
                    model=model, messages=messages)
            if debug: print(response)
            break
        except:
            print('アクセスエラー。3秒後に再試行します。')
            time.sleep(3) # 失敗したら3秒待機
    
    # APIの応答がFunction callingではなかった場合の処理 --- (*6)
    # Function Callが帰らなくなった？
    msg = response.choices[0]['message']
    
    # GPTの返答を表示、プロンプトにも追加し、終了
    if not msg.get('function_call'):
        content = msg['content']  # 応答を取り出す
        print('- AIの応答:\n', content.strip())
        # 次回の呼び出しのためにmessagesに追加
        messages.append({'role': 'assistant', 'content': content})
        return
    
    # Function Callingのパラメータを読み出す --- (*7)
    name = msg['function_call']['name']
    args = msg['function_call']['arguments']  # JSON文字列
    # インプットをリストとして取得
    if type(args) is str:  # JSONデータをデコード
        args = json.loads(msg['function_call']['arguments'])
    print('+', name, args)
    
    # 実行すべき関数を確認 --- (*8)
    # 抽出したインプットを用いて、各関数を実行
    # タスクの追加
    if name == 'add_task':
        task = args.get('task')
        # タスクのリストとタスクをインプット
        func_result = actions.add_task(todo_items, task)
    elif name == 'delete_task':
        index = args.get('index', -1)
        func_result = actions.delete_task(todo_items, index)
    elif name == 'list_tasks':
        func_result = actions.list_tasks( # ToDOの一覧を表示
            todo_items,
            args.get('mode'),
            args.get('num', 0))
        return # 一覧の表示に対してAIのコメントは不要のため
    else:
        func_result = '関数の実行に失敗しました。'
    # 関数の実行結果を含め、AIによるフォローアップメッセージを取得 --- (*9)
    messages.append({
        'role': 'function',
        'name': name,
        'content': str(func_result)  # 関数呼び出しの結果を指定
    })

    # フォローアップメッセージの取得
    call_todo_bot(messages, None)

if __name__ == '__main__':
    while True:
        # ユーザーから文章を入力 --- (*10)
        print('\n■ --- ボットへの指示を入力してください ([q]で終了)')
        user = input('>>> ')
        if user == '': continue
        if user == 'q': quit()
        # ToDOボットを実行
        messages.append({'role': 'user', 'content': user})
        call_todo_bot(messages, todo_functions.functions)
