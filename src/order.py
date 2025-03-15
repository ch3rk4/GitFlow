from src.base_quantity_purchased import BaseQuantityPurchased
from src.product import Product


class Order(BaseQuantityPurchased):
    product: Product
    buy_count: int

    def __init__(self, product: Product, buy_count: int) -> None:
        self.product = product
        self.buy_count = buy_count
        self.total_amount = 0

    def quantity_purchased(self):
        self.total_amount = self.product.price * self.buy_count
        return self.total_amount

    def apply_purchase(self) -> None:
        """Уменьшает количество товара на складе"""
        if self.product.quantity >= self.buy_count:
            self.product.quantity -= self.buy_count
        else:
            raise ValueError("Недостаточно товара на складе")

    def __str__(self) -> str:
        return f"Куплено {self.product} в количестве {self.buy_count} ед., на общую сумму {self.quantity_purchased()}р."
