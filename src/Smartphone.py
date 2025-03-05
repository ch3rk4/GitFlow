from src.product import Product

class Smartphone(Product):
    efficiency: str
    model: str
    memory: int
    color: str

    def __init__(
            self, name: str, description: str, price: float, quantity: int,
            efficiency: str, model: str, memory: int, color: str
                 ) -> None:

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError