from пмпм import load_expenses, save_expenses
from datetime import datetime
def add_expense():
    """Добавляет новый расход"""
    print("\n=== ДОБАВЛЕНИЕ РАСХОДА ===")
    try:
        amount = float(input("Сумма расхода: "))
        category = input("Категория (еда, транспорт, развлечения и т.д.): ")
        description = input("Описание: ")
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        expense = {
            "id": int(datetime.now().timestamp()),
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }
        expenses = load_expenses()
        expenses.append(expense)
        save_expenses(expenses)
        print(f"\n✓ Расход добавлен! ID: {expense['id']}")
    except ValueError:
        print("\n❌ Ошибка: Введите корректную сумму")