import json
import random

# (1) 0以上100未満の乱数を100個生成
random_numbers = [random.randint(0, 99) for _ in range(100)]

# (2) そのうち5の倍数のものだけを選択
multiples_of_5 = [num for num in random_numbers if num % 5 == 0]

# (3) 選択した数字をJSON形式に変換し表示、そして保存
json_data = json.dumps(multiples_of_5)
print(json_data)  # 標準出力に出力

# ファイル「random5.json」に保存
with open('random5.json', 'w') as file:
    file.write(json_data)
