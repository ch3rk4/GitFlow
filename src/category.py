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
        Category.products_count += len(products) if products else 0

    @property
    def products(self):
        return f"{self.name}, {self.__products} руб. Остаток: {Category.products_count}"

    def add_product(self, new_product):
        """Добавляет товар в категорию"""
        self.__products.append(new_product)
        Category.products_count += 1
