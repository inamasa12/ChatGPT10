from calc_coin import calc_coin
import pytest

def test_calc_coin():
    assert calc_coin(4570, 2, 1, 0, 9) == (2, 1, 0, 9)
    assert calc_coin(3150, 5, 0, 1, 6) == (5, 0, 1, 6)
    assert calc_coin(200, 5, 1, 1, 0) == (5, 1, 1, 0)
    assert calc_coin(3660, 6, 0, 1, 7) == (6, 0, 1, 7)
    assert calc_coin(4190, 9, 0, 1, 8) == (9, 0, 1, 8)
    assert calc_coin(3520, 2, 0, 0, 7) == (2, 0, 0, 7)
    assert calc_coin(70, 7, 0, 0, 0) == (7, 0, 0, 0)
    assert calc_coin(2060, 6, 0, 0, 4) == (6, 0, 0, 4)
    assert calc_coin(2650, 0, 1, 1, 5) == (0, 1, 1, 5)
    assert calc_coin(1550, 0, 1, 0, 3) == (0, 1, 0, 3)
