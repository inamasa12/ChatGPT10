import pytest

# こちらがテスト対象の関数です。
def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return qsort(left) + middle + qsort(right)

# 以下は pytest を使ったテストケースです。
def test_qsort():
    # 空のリスト
    assert qsort([]) == []
    # すでにソートされたリスト
    assert qsort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    # 逆順にソートされたリスト
    assert qsort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    # 同じ要素のみを含むリスト
    assert qsort([2, 2, 2]) == [2, 2, 2]
    # 異なる要素が混在するリスト
    assert qsort([3, 6, 2, 8, 4, 7]) == [2, 3, 4, 6, 7, 8]
    # 負の数を含むリスト
    assert qsort([-3, -1, -2, 0, 2]) == [-3, -2, -1, 0, 2]

# テストを実行する際は、コマンドラインで以下を入力してください:
# pytest <ファイル名>.py
