# Product and Category Management System

Проект для управления категориями товаров и продуктами, включая чтение данных из JSON-файлов и автоматическое создание объектов. Система включает классы для обработки продуктов, категорий, заказов и специальных типов товаров.

## 📦 Структура проекта
GitFlow/
├── src/
│ ├── init.py
│ ├── category.py # Класс Category 
│ ├── product.py # Класс Product
│ ├── order.py # Класс Order для обработки покупок
│ ├── base_product.py # Абстрактный базовый класс для продуктов
│ ├── base_quantity_purchased.py # Абстрактный класс для расчета покупок
│ ├── lawn_grass.py # Специализированный класс для газонной травы
│ ├── smartphone.py # Специализированный класс для смартфонов
│ ├── print_mixin.py # Миксин для печати информации
│ ├── product_iterator.py # Итератор для обхода продуктов в категории
│ ├── exception.py # Пользовательские исключения
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

## 🔄 Классы и компоненты системы

### Основные классы

1. **Product** - базовый класс товара с атрибутами: название, описание, цена, количество. Содержит:
   - Проверку на нулевое количество при создании
   - Управление ценой с запросом подтверждения при снижении
   - Фабричный метод `new_product` для создания или обновления товаров

2. **Category** - класс для управления категориями товаров:
   - Учет добавленных товаров
   - Статистика (средняя цена, общее количество)
   - Обработка исключений при добавлении товаров с нулевым количеством

3. **Order** - класс для оформления заказов:
   - Расчет общей суммы заказа
   - Уменьшение количества товара на складе
   - Проверка достаточности товаров на складе

### Специальные типы товаров

1. **LawnGrass** - газонная трава с дополнительными параметрами:
   - Страна происхождения
   - Период прорастания
   - Цвет

2. **Smartphone** - смартфоны с параметрами:
   - Производительность
   - Модель
   - Объем памяти
   - Цвет

### Служебные классы

1. **PrintMixin** - миксин для печати информации о продукте в красивом формате
2. **ProductIterator** - итератор для обхода продуктов в категории
3. **ZeroQuantity** - кастомное исключение для обработки ошибок с нулевым количеством

### Абстрактные базовые классы

1. **BaseProduct** - определяет общий интерфейс для всех продуктов
2. **BaseQuantityPurchased** - интерфейс для классов, рассчитывающих количество покупок

## 🚀 Использование

### Создание продуктов и категорий

```python
from src.product import Product
from src.category import Category

# Создание продуктов
cucumber = Product("cucumber", "smooth", 30.0, 100)
tomato = Product("tomato", "with a twig", 50.0, 80)

# Создание категории
vegetables = Category("Vegetables", "Healthy food", [cucumber, tomato])

# Добавление продукта в категорию
carrot = Product("carrot", "orange", 45.0, 120)
vegetables.add_product(carrot)

# Получение статистики
print(f"Средняя цена: {vegetables.avg_sum()}")
print(f"Всего продуктов: {vegetables.quantity_purchased()}")
```

### Создание специальных типов товаров

```python
from src.lawn_grass import LawnGrass
from src.smartphone import Smartphone

# Газонная трава
grass = LawnGrass(
    name="Premium Grass", 
    description="Beautiful lawn", 
    price=1500.0, 
    quantity=50,
    country="Netherlands",
    germination_period=14.0,
    color="Bright Green"
)

# Смартфон
phone = Smartphone(
    name="SuperPhone X",
    description="Flagship model",
    price=50000.0,
    quantity=10,
    efficiency=95,
    model="X2022",
    memory=256,
    color="Black"
)
```

### Оформление заказа

```python
from src.order import Order

# Создаем заказ
order = Order(product=cucumber, buy_count=5)

# Рассчитываем сумму
total = order.quantity_purchased()
print(f"Сумма заказа: {total} руб.")

# Применяем заказ (уменьшаем количество на складе)
order.apply_purchase()
```

### Работа с JSON файлами

```python
from src.work_with_json import create_object_from_json, read_json

# Загрузка данных
raw_data = read_json("data/products.json")
categories = create_object_from_json(raw_data)

# Вывод загруженных категорий
for category in categories:
    print(f"Категория: {category.name}")
    for product_str in category.products:
        print(f"  - {product_str}")
```

## 📝 Пример данных (data/products.json)
```json
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
      },
      {
        "name": "tomato",
        "description": "with a twig",
        "price": 50.0,
        "quantity": 80
      }
    ]
  },
  {
    "name": "Electronics",
    "description": "Gadgets",
    "products": [
      {
        "name": "Smartphone",
        "description": "Latest model",
        "price": 45000.0,
        "quantity": 20
      }
    ]
  }
]
```

## 🧪 Тестирование

```bash
# Запуск всех тестов с покрытием
pytest --cov=src --cov-report=html

# Только запуск тестов
pytest tests/
```

### Что проверяют тесты:

1. Корректность инициализации объектов Product и Category.
2. Подсчет количества категорий и продуктов.
3. Изоляция тестов через сброс статических переменных (реализовано в conftest.py).
4. Обработка исключений при добавлении товаров с нулевым количеством.
5. Проверка работы блока finally в методе add_product.
6. Проверка сценария, когда quantity изменили после создания объекта.
7. Корректность операции добавления продуктов (метод `__add__`).
8. Проверка фабричного метода new_product.

### Пример теста на обработку исключений ZeroQuantity

```python
def test_add_product_with_modified_zero_quantity(capsys, first_category):
    """
    Проверяет обработку исключения ZeroQuantity, когда количество товара
    изменили на нулевое после создания объекта.
    """
    # Создаем продукт с допустимым начальным количеством
    product = Product(name="beef", description="ribeye", price=300.0, quantity=1)
    
    # Изменяем quantity на 0 после создания
    product.quantity = 0
    
    # Пытаемся добавить продукт в категорию
    first_category.add_product(product)
    
    # Получаем вывод из консоли
    output = capsys.readouterr()
    
    # Проверяем, что продукт НЕ был добавлен и блок finally выполнился
    assert "товар добавлен" not in output.out
    assert "Обработка добавления товара завершена" in output.out
```

## 📊 Отчёт о покрытии
После запуска тестов с ```--cov-report=html``` откройте htmlcov/index.html в браузере для просмотра детального отчета о покрытии кода тестами.

## 🔍 Особенности реализации

- **Обработка исключений**: Система имеет двойную защиту от товаров с нулевым количеством - и в конструкторе Product, и в методе add_product класса Category
- **Сброс состояния**: Фикстура ```reset_class_variables``` обнуляет счётчики перед каждым тестом
- **Работа с JSON**: Автоматическое создание объектов из структурированных JSON файлов
- **Итерация по продуктам**: Специальный класс ProductIterator для удобного обхода продуктов в категории
- **Наследование**: Система демонстрирует использование как абстрактных классов, так и конкретных наследников
- **Миксины**: Использование PrintMixin для расширения функциональности классов

## ⚠️ Известные ограничения

- Атрибут quantity в Product является публичным, что позволяет изменить его на некорректное значение после создания объекта
- При снижении цены требуется интерактивное подтверждение пользователя, что может быть неудобно в автоматизированных сценариях