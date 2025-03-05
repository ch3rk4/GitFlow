from typing import Generator

import pytest

from src.category import Category
from src.product import Product
from src.products_iterator import ProductIterator
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


@pytest.fixture(autouse=True)
def reset_class_variables() -> Generator:
    Category.categories_count = 0
    Category.products_count = 0
    yield


@pytest.fixture()
def first_category() -> Category:
    return Category(
        name="Vegetables",
        description="Healthy food",
        products=[
            Product("cucumber", "smooth", 30.0, 100),
            Product("tomato", "with a twig", 50.0, 80),
        ],
    )


@pytest.fixture()
def second_category() -> Category:
    return Category(
        name="Dietary meat",
        description="Healthy meat",
        products=[
            Product("chicken", "drumstick", 150.0, 50),
            Product("rabbit", "carcass", 500.0, 10),
            Product("turkey", "breast", 200.0, 40),
        ],
    )


@pytest.fixture()
def product() -> Product:
    return Product(name="chicken", description="drumstick", price=150.0, quantity=50)


@pytest.fixture()
def product2() -> Product:
    return Product(name="cucumber", description="smooth", price=50.0, quantity=20)


@pytest.fixture()
def products_iterator(first_category: Category) -> ProductIterator:
    return ProductIterator(first_category)


@pytest.fixture()
def smartphone1() -> Smartphone:
    return Smartphone('Iphone', 'Glade', 300, 1000, 1200, 'XR', 128, 'black')


@pytest.fixture()
def smartphone2() -> Smartphone:
    return Smartphone('Samsung', 'Flip', 300, 1000, 1500, 'S20', 1000, 'blue')


@pytest.fixture()
def lawn_grass1() -> LawnGrass:
    return LawnGrass('Green grass', 'Green grass', 1500, 10000, 'England', 6, 'black')


@pytest.fixture()
def lawn_grass2() -> LawnGrass:
    return LawnGrass('Black grass', 'Green grass', 1500, 10000, 'Nigeria', 6, 'green')


