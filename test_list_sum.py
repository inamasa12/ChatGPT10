import pytest

# sum_list関数のダミー実装
def sum_list(a_list):
    return sum(a_list)

# sum_list関数をテストするテストケース
def test_sum_list():
    assert sum_list([1, 2, 3]) == 6, "1, 2, 3の合計は6になるべき"
    assert sum_list([]) == 0, "空のリストの合計は0になるべき"
    assert sum_list([-1, 1]) == 0, "−1と1の合計は0になるべき"
    assert sum_list([1.5, 2.5, 3]) == 7, "1.5, 2.5, 3の合計は7になるべき"
