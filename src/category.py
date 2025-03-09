from src.product import Product
from src.base_quantity_purchased import BaseQuantityPurchased


class Category(BaseQuantityPurchased):
    """Класс формирует категорию 'Категория'"""

    name: str
    description: str
    products: list
    all_products: int
    product_sum: int

    categories_count = 0
    products_count = 0

    def __init__(
        self, name: str, description: str, products: list[Product] = None
    ) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []
        self.all_products = 0
        self.product_sum = 0

        Category.categories_count += 1
        Category.products_count += len(self.__products) if products else 0

    def quantity_purchased(self):
        self.all_products = sum(product.quantity for product in self.__products)
        return self.all_products

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.quantity_purchased()} шт."

    @property
    def products(self) -> list:
        return [str(product) for product in self.__products]

    def add_product(self, new_product) -> None:
        """Добавляет товар в категорию"""
        self.__products.append(new_product)
        Category.products_count += 1

    @property
    def products_list(self) -> list:
        return self.__products
