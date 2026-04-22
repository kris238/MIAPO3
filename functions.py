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

def view_expenses():
    """Просмотр всех расходов"""
    print("\n=== ВСЕ РАСХОДЫ ===")

    expenses = load_expenses()

    if not expenses:
        print("Нет добавленных расходов")
        return

    print(f"\n{'ID':<10} {'Сумма':<10} {'Категория':<15} {'Дата':<20} {'Описание'}")
    print("-" * 70)

    for exp in expenses:
        print(f"{exp['id']:<10} {exp['amount']:<10.2f} {exp['category']:<15} "
              f"{exp['date']:<20} {exp['description']}")

    total = sum(exp['amount'] for exp in expenses)
    print("-" * 70)
    print(f"ИТОГО: {total:.2f} руб.")