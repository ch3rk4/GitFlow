import json
import os

from src.product import Product
from src.category import Category


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as file:
        products = json.load(file)
    return products


def create_object_from_json(data: dict) -> list:
    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products
        categories.append(Category(**category))

    return categories
