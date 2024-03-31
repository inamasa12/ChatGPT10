def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()  # リストの最後の要素をピボットとして取り出す
        less = []  # ピボットより小さい要素
        greater = []  # ピボットより大きい要素
        for x in arr:
            if x <= pivot:
                less.append(x)
            else:
                greater.append(x)
        return qsort(less) + [pivot] + qsort(greater)  # 分割したリストを再帰的にソートして結合

# サンプルのリスト
sample_list = [3, 6, 8, 10, 1, 2, 1]

# qsort関数を呼び出してリストをソート
sorted_list = qsort(sample_list)

# ソートされたリストを表示
print(sorted_list)
