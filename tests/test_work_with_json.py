import json
import os.path
from typing import Any, Dict
from unittest.mock import mock_open, patch

import pytest

from src.work_with_json import create_object_from_json, read_json


class TestReadJson:
    """Тесты для функции чтения JSON-файлов"""

    @patch("builtins.open", new_callable=mock_open())
    @patch("json.load")
    def test_successful_read(self, mock_json_load: Any, mock_file: Any) -> None:
        """Тест успешного чтения JSON-файла"""
        test_data: Dict[str, Any] = {"test": "data"}
        mock_json_load.return_value = test_data

        result = read_json("test_path.json")

        mock_file.assert_called_once_with(
            os.path.abspath("test_path.json"), "r", encoding="UTF-8"
        )

        mock_json_load.assert_called_once()

        assert result == test_data

    @patch("builtins.open")
    def test_file_not_found(self, mock_file: Any) -> None:
        """Тест обработки ошибки при отсутствии файла"""
        mock_file.side_effect = FileNotFoundError()

        with pytest.raises(FileNotFoundError):
            read_json("nonexistent.json")

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.load")
    def test_invalid_json(self, mock_json_load: Any, mock_file: Any) -> None:
        mock_json_load.side_effect = json.JSONDecodeError("Test error", "dco", 1)

        with pytest.raises(json.JSONDecodeError):
            read_json("invalid.json")


class TestCreateObjectFromJson:
    """Тесты для функции создания объектов из json-файлов"""

    @patch("src.work_with_json.Category")
    @patch("src.work_with_json.Product")
    def test_successful_creation(self, mock_product: Any, mock_category: Any) -> None:
        """Тестирует успешное создание объектов"""
        test_data = [
            {
                "name": "Категория",
                "description": "Описание",
                "products": [
                    {
                        "name": "Продукт",
                        "description": "Описание",
                        "price": 100.0,
                        "quantity": 1,
                    }
                ],
            }
        ]

        mock_product.return_value = "mocked_product"
        mock_category.return_value = "mocked_category"

        result = create_object_from_json(test_data)

        mock_product.assert_called_with(
            name="Продукт", description="Описание", price=100.0, quantity=1
        )

        mock_category.assert_called_with(
            name="Категория", description="Описание", products=["mocked_product"]
        )

    def test_empty_data(self) -> None:
        """Тест создания объектов из пустых данных"""
        result = create_object_from_json([])
        assert isinstance(result, list)
        assert len(result) == 0

    @patch("src.work_with_json.Category")
    def test_invalid_data(self, mock_category: Any) -> None:
        """Тест обработки некорректных данных"""
        test_data = [{"invalid_field": "value", "products": []}]
        mock_category.side_effect = TypeError("Invalid data")

        with pytest.raises(TypeError):
            create_object_from_json(test_data)
