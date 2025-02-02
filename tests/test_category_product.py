from src.category import Category
from src.product import Product


def test_product_init(product: Product) -> None:
    assert product.name == 'chicken'
    assert product.description == 'drumstick'
    assert product.price == 150.0
    assert product.quantity == 50

def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == 'Vegetables'
    assert first_category.description == 'Healthy food'
    assert len(first_category.products) == 2

    assert second_category.name == 'Dietary meat'
    assert second_category.description == 'Healthy meat'
    assert len(second_category.products) == 3

def test_categories_count(first_category: Category, second_category: Category) -> None:
    assert first_category.categories_count == 2
    assert second_category.categories_count == 2

def test_products_count(first_category: Category, second_category: Category) -> None:
    assert first_category.products_count == 5
    assert second_category.products_count == 5