# Product and Category Management System

Проект для управления категориями товаров и продуктами, включая чтение данных из JSON-файлов и автоматическое создание объектов.

## 📦 Структура проекта
GitFlow/
├── src/
│ ├── init.py
│ ├── category.py # Класс Category
│ ├── product.py # Класс Product
│ └── work_with_json.py # Работа с JSON
├── tests/
│ ├── init.py
│ ├── conftest.py # Фикстуры для тестов
│ └── test_category_product.py
├── data/
│ └── products.json # Пример данных (создайте самостоятельно)
├── pyproject.toml
└── README.md


## 🛠️ Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/ваш-репозиторий.git
```

2. Установите зависимости:
```bash
pip install pytest pytest-cov
```

# Использование
## Запуск программы
```bash
# main.py
from src.work_with_json import create_object_from_json, read_json

raw_data = read_json("data/products.json")
categories = create_object_from_json(raw_data)
print(categories)  # Вывод всех категорий и продуктов
```

## Пример данных (data/products.json)
```bash
[
  {
    "name": "Vegetables",
    "description": "Healthy food",
    "products": [
      {
        "name": "cucumber",
        "description": "smooth",
        "price": 30.0,
        "quantity": 100
      }
    ]
  }
]
```

# Тестирование
```bash
# Запуск всех тестов с покрытием
pytest --cov=src --cov-report=html

# Только запуск тестов
pytest tests/
```

## Что проверяют тесты:
1. Корректность инициализации объектов Product и Category.

2. Подсчет количества категорий и продуктов.

3. Изоляция тестов через сброс статических переменных (реализовано в conftest.py).

# Отчёт о покрыктии
После запуска тестов с ```--cov-report=html``` откройте htmlcov/index.html в браузере.

# Особенности реализации
- Сброс состояния: фикстура ```reset_class_variables``` обнуляет счётчики перед каждым тестом
- Работа с json