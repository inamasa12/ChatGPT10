import csv
import json

# 入力ファイルと出力ファイルのパス
input_file = 'ninja_corpus.csv'
output_file = 'ninja_corpus.jsonl'

# CSVファイルを読み込み、JSONL形式のファイルを作成する
with open(input_file, 'r', encoding='utf-8') as csvfile, open(output_file, 'w', encoding='utf-8') as jsonlfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # ヘッダー行を読み飛ばす
    for row in reader:
        json_record = {"prompt": row[0], "completion": row[1]}
        jsonlfile.write(json.dumps(json_record, ensure_ascii=False) + '\n')

print(f"JSONLファイル '{output_file}' が正常に作成されました。")
