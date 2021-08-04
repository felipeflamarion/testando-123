from .calculator import add, sub, mul, div


def test_add():
    assert add(2, 2) == 4


def test_sub():
    assert sub(2, 2) == 0


def test_mul():
    assert mul(2, 2) == 4


def test_div():
    assert div(2, 2) == 1