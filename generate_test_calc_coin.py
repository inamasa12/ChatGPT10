import random

print("from calc_coin import calc_coin")
print("import pytest")
print()
print("def test_calc_coin():")
for _ in range(10):  # テストケースの数を10に変更
    a = random.randint(0, 9)
    d = random.randint(0, 9)
    b = random.randint(0, 1)
    c = random.randint(0, 1)
    
    total = 10 * a + 50 * b + 100 * c + 500 * d
    
    print(f"    assert calc_coin({total}, {a}, {b}, {c}, {d}) == ({a}, {b}, {c}, {d})")
