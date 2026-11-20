import pytest

from orderlab.pricing import subtotal


def test_subtotal_normal():
    price = 10_000
    quantity = 2

    result = subtotal(price, quantity)
    assert result == 20_000


def test_subtotal_zero():
    assert subtotal(0, 3) == 0


def test_subtotal_negative():
    with pytest.raises(ValueError):
        subtotal(-100, 2)
        
def test_subtotal_outlier():
    with pytest.raises(ValueError):
        subtotal(8000, 10_0000)
