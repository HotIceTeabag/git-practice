def subtotal(unit_price: int, quantity: int) -> int:
    if unit_price < 0 or quantity < 0:
        raise ValueError("negative input")
    if unit_price > 100_000 or quantity >= 1_0000:
        raise ValueError("outlier value")
    return unit_price * quantity


def final_total(price: int, qty: int, discount: int) -> int:
    if not 0 <= discount <= 100:
        raise ValueError("invalid discount")
    amount = subtotal(price, qty)
    amount -= amount * discount // 100
    shipping = 3_000 if 0 < amount < 50_000 else 0
    return amount + shipping
