import pytest

from src.category import Category
from src.product import Product

@pytest.fixture()
def first_category() -> Category:
    return Category(
        name='Vegetables',
        description='Healthy foods',
        products=[
            Product('cucumber', 'smooth', 30.0, 100),
            Product('tomato', 'with a twig', 50.0, 80)
        ]
    )

@pytest.fixture()
def second_category() -> Category:
    return Category(
        name='Dietary meat',
        description='Healthy meat',
        products=[
            Product('chicken', 'drumstick', 150.0, 50),
            Product('rabbit', 'carcass', 500.0, 10),
            Product('turkey', 'breast', 200.0, 40)
        ]
    )

@pytest.fixture()
def product() -> Product:
    return Product(
        name='chicken',
        description='drumstick',
        price=150.0,
        quantity=50
    )