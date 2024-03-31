# Flaskライブラリをインポートします。Flaskは、Webアプリケーションを構築するためのフレームワークです。
from flask import Flask, request, jsonify, send_from_directory

# Flaskアプリケーションのインスタンスを作成します。template_folderパラメータにより、テンプレートファイルのディレクトリを指定しています。
app = Flask(__name__, template_folder='./')

# ToDoタスクを保存するファイル名を定義します。
TASKS_FILE = 'todo_tasks.txt'

@app.route('/')
def home():
    # ルートディレクトリにアクセスされた場合、クライアント側のHTMLファイルを返します。
    return send_from_directory('.', 'todo_client.html')

@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    # タスクを取得するエンドポイント。GETリクエストに対応します。
    with open(TASKS_FILE, 'r', encoding='utf-8') as file:
        # ファイルからタスクのリストを読み込みます。
        tasks = file.readlines()
    # 各タスクから末尾の改行を削除します。
    tasks = [task.strip() for task in tasks]
    # タスクのリストをJSON形式でクライアントに返します。
    return jsonify(tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    # 新しいタスクを追加するエンドポイント。POSTリクエストに対応します。
    # リクエストのJSONボディからタスクを取得します。
    task = request.json['task']
    with open(TASKS_FILE, 'a', encoding='utf-8') as file:
        # タスクをファイルに追記します。
        file.write(task + '\n')
    # 処理の成功をクライアントに伝えます。
    return jsonify({'status': 'success'})

# スクリプトが直接実行された場合にのみ、Webサーバーを起動します。
if __name__ == '__main__':
    app.run(debug=True)
