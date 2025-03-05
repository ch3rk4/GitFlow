from src.category import Category


class ProductIterator:

    category: Category

    def __init__(self, product: Category) -> None:
        if not isinstance(product, Category):
            raise ValueError("Класс должен существовать")

        self.category = product
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.products_list):
            product = self.category.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
