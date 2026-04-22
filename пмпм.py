import json
import os
DATA_FILE = "expenses.json"
def load_expenses():
    """Загружает расходы из файла"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)
def save_expenses(expenses):
    """Сохраняет расходы в файл"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)