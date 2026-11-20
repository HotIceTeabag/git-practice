import pytest

from orderlab.pricing import final_total, subtotal


def test_subtotal_normal():
    price = 10_000
    quantity = 2

    result = subtotal(price, quantity)
    assert result == 20_000


def test_subtotal_zero():
    assert subtotal(0, 3) == 0


def test_subtotal_negative():
    with pytest.raises(ValueError, match="negative input"):
        subtotal(-100, 2)


def test_subtotal_outlier():
    with pytest.raises(ValueError, match="outlier value"):
        subtotal(8000, 100000)


def test_discount_over_100():
    with pytest.raises(ValueError, match="invalid discount"):
        final_total(10000, 20, 101)


def test_discount_below_zero():
    with pytest.raises(ValueError, match="invalid discount"):
        final_total(10000, 20, -1)


@pytest.mark.parametrize(
    "price, qty, discount, expected",
    [
        (10000, 2, 0, 23000),
        (49999, 1, 0, 52999),
        (50000, 1, 0, 50000),
        (50001, 1, 0, 50001),
        (10000, 2, 10, 21000),
    ],
)
def test_final_total(price, qty, discount, expected):
    assert final_total(price, qty, discount) == expected
