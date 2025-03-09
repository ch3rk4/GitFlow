import pytest

from src.order import Order
from src.category import Category
from src.product import Product


def test_order_init():
    order = Order(Product("chicken", "drumstick", 150.0, 50), 10)
    assert str(order.product) == str(Product('chicken', 'drumstick', 150.0, 50))
    assert order.buy_count == 10


def test_quantity_purchased():
    order = Order(Product("chicken", "drumstick", 150.0, 50), 10)
    assert order.quantity_purchased() == 1500


def test_apply_purchase(product):
    initial_quantity = product.quantity
    order = Order(product, 10)
    order.quantity_purchased()
    order.apply_purchase()
    assert product.quantity == initial_quantity - 10


def test_apply_purchase_error(product):
    with pytest.raises(ValueError, match="Недостаточно товара на складе") as e:
        order = Order(product, 60)
        order.apply_purchase()

    assert product.quantity == 50
