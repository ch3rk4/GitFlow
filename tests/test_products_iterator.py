from unittest.mock import patch

import pytest

from src.category import Category
from src.product import Product
from src.products_iterator import ProductIterator


def test_isinstance_products(first_category: Category) -> None:
    instance = ProductIterator(first_category)

    assert instance.category == first_category


@pytest.mark.parametrize("invalid_value", ["test", 123, None, object(), []])
def test_init_with_invalid_types_parametrized(invalid_value) -> None:
    with pytest.raises(ValueError) as e:
        ProductIterator(invalid_value)

    assert str(e.value) == "Класс должен существовать"


def test_products_iterator(products_iterator: ProductIterator) -> None:
    assert products_iterator.index == 0
    assert next(products_iterator).name == "cucumber"
