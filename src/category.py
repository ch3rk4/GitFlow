class Category:
    name: str
    description: str
    products: list

    categories_count = 0
    products_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.categories_count += 1
        Category.products_count = len(products) if products else 0
