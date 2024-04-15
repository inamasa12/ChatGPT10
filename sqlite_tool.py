import sqlite3
import sys

# SQLを実行する関数
def execute_sql(cursor, sql):
    try:
        # SQLコマンドを実行
        cursor.execute(sql)
        # SELECT文の場合、結果を表示
        if sql.strip().upper().startswith('SELECT'):
            rows = cursor.fetchall()  # 結果の行を全て取得
            if rows:
                # カラム名（ヘッダ）を取得して表示
                headers = [description[0] for description in cursor.description]
                print(' | '.join(headers))
                # 各行のデータを表示
                for row in rows:
                    print(' | '.join(str(r) for r in row))
            else:
                print("No results.")
        else:
            # SELECT文以外の場合、成功したことを通知
            print(f"Executed successfully: {sql}")
    except sqlite3.Error as e:
        # SQL実行エラー時にエラーメッセージを表示
        print(f"An error occurred: {e}")

# メイン関数
def main(db_file):
    # データベースに接続
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    print("SQLite Command Line Tool. Enter SQL commands or 'exit;' to quit.")
    lines = []

    while True:
        line = input()
        # 'exit;'が入力されたら終了
        if line.strip().lower() == 'exit;':
            break
        lines.append(line)
        # SQL文が「;」で終わる場合、SQLを実行
        if line.endswith(';'):
            sql = ' '.join(lines)
            execute_sql(cursor, sql)
            lines = []  # 次のSQL入力のためにリセット

    connection.close()  # データベース接続を閉じる

if __name__ == '__main__':
    # コマンドライン引数が足りない場合は使い方を表示
    if len(sys.argv) < 2:
        print("Usage: python script.py <database_file>")
        sys.exit(1)

    # データベースファイル名を取得してメイン関数を実行
    db_file = sys.argv[1]
    main(db_file)
