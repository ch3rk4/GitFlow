from unittest.mock import patch

import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_product_init(product: Product) -> None:
    assert product.name == "chicken"
    assert product.description == "drumstick"
    assert product.price == 150.0
    assert product.quantity == 50


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Vegetables"
    assert first_category.description == "Healthy food"
    assert len(first_category.products_list) == 2

    assert second_category.name == "Dietary meat"
    assert second_category.description == "Healthy meat"
    assert len(second_category.products_list) == 3


def test_categories_count(first_category: Category, second_category: Category) -> None:
    assert first_category.categories_count == 2
    assert second_category.categories_count == 2


def test_products_count(first_category: Category, second_category: Category) -> None:
    assert first_category.products_count == 5
    assert second_category.products_count == 5


def test_products_property(first_category: Category) -> None:
    assert first_category.products == (
        ["cucumber, 30.0 руб. Остаток: 100 шт.", "tomato, 50.0 руб. Остаток: 80 шт."]
    )


def test_products_list_property(first_category: Category) -> None:
    assert len(first_category.products) == 2


def test_add_product(first_category: Category, product: Product) -> None:
    first_category.add_product(product)
    assert len(first_category.products) == 3
    assert Category.products_count == 3


def test_price_property(product: Product) -> None:
    assert product.price == 150.0


def test_price_setter_successful(product: Product) -> None:
    product.price = 160.0
    assert product.price == 160.0


def test_price_setter_below_zero(product: Product) -> None:
    with pytest.raises(ValueError) as e:
        product.price = -50.0

    assert str(e.value) == "Цена должна быть положительной"


def test_price_setter_lower_successful(product: Product) -> None:
    with patch("builtins.input", return_value="y") as mock_input:
        product.price = 140.0

        assert product.price == 140.0

        mock_input.assert_called_with(
            "Подтвердите понижение цены товара: введите 'y' (yes) или 'n'(no)"
        )


def test_price_setter_lower_not_successful(product: Product) -> None:
    with patch("builtins.input", return_value="n") as mock_input, patch(
        "builtins.print"
    ) as mock_print:
        product.price = 140.0

        assert product.price == 150.0

        mock_input.assert_called_with(
            "Подтвердите понижение цены товара: введите 'y' (yes) или 'n'(no)"
        )

        mock_print.assert_called_with("Вы отказались понижать цену")


def test_price_setter_lower_while(product: Product) -> None:
    input_response = ["a", "y"]

    with patch("builtins.input", side_effect=input_response) as mock_input, patch(
        "builtins.print"
    ) as mock_print:
        product.price = 140.0

        assert product.price == 140.0

        assert mock_input.call_count == 2
        mock_input.assert_called_with(
            "Подтвердите понижение цены товара: введите 'y' (yes) или 'n'(no)"
        )
        mock_print.assert_called_with("Некорректный ответ! Введите 'y' или 'n'")


def test_new_product_create() -> None:
    new_product = Product("tomato", "red", 70.0, 50)
    new_product.name = "tomato"
    new_product.description = "red"
    new_product.__price = 70.0
    new_product.quantity = 50


class TestProduct:
    """Тесты для метода new_product класса Product"""

    def test_new_product_with_invalid_objects(self):
        class FakeProduct:
            def __init__(self, name):
                self.name = name

        invalid_products = [FakeProduct("Fake")]

        with pytest.raises(TypeError) as e:
            Product.new_product(
                name="Test Product",
                description="Test",
                price=100.0,
                quantity=5,
                products=invalid_products,
            )

        assert str(e.value) == (
            "Объект FakeProduct instance не является экземпляром класса Product"
        ).replace("FakeProduct instance", str(invalid_products[0]))

    def test_new_product_with_valid_objects(self):
        valid_product = [Product("Valid product", "valid", 200.0, 10)]

        try:
            Product.new_product(
                name="Test Product",
                description="Test",
                price=100.0,
                quantity=5,
                products=valid_product,
            )
        except TypeError:
            pytest.fail("Unexpected TypeError for valid products")


def test_product_str(product):
    assert str(product) == "chicken, 150.0 руб. Остаток: 50 шт."


def test_category_str(first_category):
    assert str(first_category) == "Vegetables, количество продуктов: 180 шт."


def test_add_products(product, product2):
    assert product + product2 == 8500


def test_smartphone_init(smartphone1: Smartphone) -> None:
    assert smartphone1.name == "Iphone"
    assert smartphone1.description == "Glade"
    assert smartphone1.price == 300
    assert smartphone1.quantity == 1000
    assert smartphone1.efficiency == 1200
    assert smartphone1.model == "XR"
    assert smartphone1.memory == 128
    assert smartphone1.color == "black"


def test_smartphone_add(smartphone1: Smartphone, smartphone2: Smartphone) -> None:
    assert smartphone1 + smartphone2 == 600000


def test_smartphone_add_error(smartphone1: Smartphone) -> None:
    with pytest.raises(TypeError):
        res = smartphone1 + 20


def test_lawn_grass_init(lawn_grass1: LawnGrass) -> None:
    assert lawn_grass1.name == "Green grass"
    assert lawn_grass1.description == "Green grass"
    assert lawn_grass1.price == 1500
    assert lawn_grass1.quantity == 10000
    assert lawn_grass1.country == "England"
    assert lawn_grass1.germination_period == 6
    assert lawn_grass1.color == "black"


def test_lawn_grass_add(lawn_grass1: LawnGrass, lawn_grass2: LawnGrass) -> None:
    assert lawn_grass1 + lawn_grass2 == 30000000


def test_lawn_grass_add_error(lawn_grass1: LawnGrass) -> None:
    with pytest.raises(TypeError):
        res = lawn_grass1 + 10


def test_add_error(
    product: Product, smartphone1: Smartphone, lawn_grass1: LawnGrass
) -> None:
    with pytest.raises(TypeError):
        res1 = product + smartphone1
        res2 = product + lawn_grass1
        res3 = smartphone1 + lawn_grass1


def test_product_init_error() -> None:

    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        new_prod = Product('cucumber', 'cucumber', 30.0, 0)


def test_avg_sum(first_category):
    assert Category.avg_sum(first_category) == 40.0


def test_avg_sum_error() -> None:
    cat1 = Category("name", "descr", [])

    assert Category.avg_sum(cat1) == 0
