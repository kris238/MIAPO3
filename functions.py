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
    """Просмотр всех расходов (с нумерацией для удобства)"""
    print("\n=== ВСЕ РАСХОДЫ ===")

    expenses = load_expenses()

    if not expenses:
        print("Нет добавленных расходов")
        return

    print(f"\n{'№':<3} {'ID':<10} {'Сумма':<10} {'Категория':<15} {'Дата':<20} {'Описание'}")
    print("-" * 80)

    for idx, exp in enumerate(expenses, 1):
        print(f"{idx:<3} {exp['id']:<10} {exp['amount']:<10.2f} "
              f"{exp['category']:<15} {exp['date']:<20} {exp['description'][:20]}")

    total = sum(exp['amount'] for exp in expenses)
    print("-" * 80)
    print(f"ИТОГО: {total:.2f} руб.")


def delete_expense():
    """Удаляет расход по ID"""
    print("\n=== УДАЛЕНИЕ РАСХОДА ===")

    expenses = load_expenses()

    if not expenses:
        print("Нет расходов для удаления")
        return
    print("\nТекущие расходы:")
    print(f"{'ID':<10} {'Сумма':<10} {'Категория':<15} {'Описание'}")
    print("-" * 50)
    for exp in expenses:
        print(f"{exp['id']:<10} {exp['amount']:<10.2f} {exp['category']:<15} "
              f"{exp['description'][:20]}")

    try:
        expense_id = int(input("\nВведите ID расхода для удаления: "))

        expense_to_delete = None
        for exp in expenses:
            if exp['id'] == expense_id:
                expense_to_delete = exp
                break

        if expense_to_delete:
            print(f"\nРасход к удалению:")
            print(f"  Сумма: {expense_to_delete['amount']} руб.")
            print(f"  Категория: {expense_to_delete['category']}")
            print(f"  Описание: {expense_to_delete['description']}")

            confirm = input("\nПодтверждаете удаление? (y/n): ")
            if confirm.lower() == 'y':
                expenses.remove(expense_to_delete)
                save_expenses(expenses)
                print("✓ Расход успешно удален")
            else:
                print("Удаление отменено")
        else:
            print("❌ Расход с таким ID не найден")
    except ValueError:
        print("❌ Ошибка: ID должен быть числом")