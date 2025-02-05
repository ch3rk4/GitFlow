from src.work_with_json import create_object_from_json, read_json

raw_data = read_json("C:/Users/petys/PycharmProjects/GitFlow/data/products.json")
categories_data = create_object_from_json(raw_data)

print(categories_data)
