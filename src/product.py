class Product:
    """Класс формирует категорию 'Продукты'"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            raise ValueError("Цена должна быть положительной")
        if hasattr(self, "_Product__price") and new_price < self.__price:
            while True:
                user_answer = input(
                    "Подтвердите понижение цены товара: введите 'y' (yes) или 'n'(no)"
                ).lower()
                if user_answer == 'y':
                    self.__price = new_price
                    break
                elif user_answer == 'n':
                    print("Вы отказались понижать цену")
                    break
                else:
                    print("Некорректный ответ! Введите 'y' или 'n'")
        else:
            self.__price = new_price


    @classmethod
    def new_product(
            cls, name: str, description: str, price: float, quantity: int, products: list
    ) -> 'Product':
        for product in products:
            if product.name == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product
        new_product = cls(name, description, price, quantity)
        products.append(new_product)
        return new_product

