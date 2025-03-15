from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
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

        if self.quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        super().__init__()
        PrintMixin.__init__(self)


    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            raise ValueError("Цена должна быть положительной")
        if hasattr(self, "_Product__price") and new_price < self.__price:
            while True:
                user_answer = input(
                    "Подтвердите понижение цены товара: введите 'y' (yes) или 'n'(no)"
                ).lower()
                if user_answer == "y":
                    self.__price = new_price
                    break
                elif user_answer == "n":
                    print("Вы отказались понижать цену")
                    break
                else:
                    print("Некорректный ответ! Введите 'y' или 'n'")
        else:
            self.__price = new_price

    @classmethod
    def new_product(
        cls, name: str, description: str, price: float, quantity: int, products: list
    ) -> "Product":

        for product in products:
            if not isinstance(product, cls):
                raise TypeError(
                    f"Объект {product} не является экземпляром класса Product"
                )
        for product in products:
            if product.name == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product
        new_product = cls(name, description, price, quantity)
        products.append(new_product)
        return new_product
