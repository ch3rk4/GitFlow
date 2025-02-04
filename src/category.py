from typing import Any


class Category:
    """Класс формирует категорию 'Категория'"""

    name: str
    description: str
    products: list

    categories_count = 0
    products_count = 0

    def __init__(self, name: str, description: str, products: list[Any] = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.categories_count += 1
        Category.products_count += len(self.__products) if products else 0

    @property
    def products(self) -> list:
        return [
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        ]

    def add_product(self, new_product) -> None:
        """Добавляет товар в категорию"""
        self.__products.append(new_product)
        Category.products_count += 1

    @property
    def products_list(self) -> list:
        return self.__products
