import os
import json

# Чтение json файла
def read(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())

# Запись в json файл
def write(path: str, data: dict):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))