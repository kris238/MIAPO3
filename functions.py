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
        print("\n Ошибка: Введите корректную сумму")

def view_expenses():
    """Просмотр всех расходов (улучшенный формат с подробным описанием)"""
    print("\n=== ВСЕ РАСХОДЫ ===")

    expenses = load_expenses()

    if not expenses:
        print("Нет добавленных расходов")
        return

    for idx, exp in enumerate(expenses, 1):
        print(f"\n{idx}. РАСХОД #{exp['id']}")
        print(f"Дата: {exp['date']}")
        print(f"Сумма: {exp['amount']} руб.")
        print(f"Категория: {exp['category']}")
        print(f"Описание: {exp['description']}")
        print("   " + "-" * 30)

    total = sum(exp['amount'] for exp in expenses)
    print(f"\nВСЕГО РАСХОДОВ: {total:.2f} руб.")


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
            print(" Расход с таким ID не найден")
    except ValueError:
        print(" Ошибка: ID должен быть числом")


def edit_expense():
    """Редактирует существующий расход"""
    print("\n=== РЕДАКТИРОВАНИЕ РАСХОДА ===")

    expenses = load_expenses()

    if not expenses:
        print("Нет расходов для редактирования")
        return

    print("\nТекущие расходы:")
    print(f"{'ID':<10} {'Сумма':<10} {'Категория':<15} {'Описание'}")
    print("-" * 50)
    for exp in expenses:
        print(f"{exp['id']:<10} {exp['amount']:<10.2f} {exp['category']:<15} "
              f"{exp['description'][:20]}")

    try:
        expense_id = int(input("\nВведите ID расхода для редактирования: "))

        for exp in expenses:
            if exp['id'] == expense_id:
                print(f"\nТекущие данные:")
                print(f"1. Сумма: {exp['amount']} руб.")
                print(f"2. Категория: {exp['category']}")
                print(f"3. Описание: {exp['description']}")
                print(f"4. Дата: {exp['date']}")

                print("\nЧто хотите изменить?")
                print("1. Сумму")
                print("2. Категорию")
                print("3. Описание")
                print("4. Выйти без изменений")

                field_choice = input("Ваш выбор (1-4): ")

                if field_choice == '1':
                    new_amount = float(input("Новая сумма: "))
                    exp['amount'] = new_amount
                    print("✓ Сумма обновлена")
                elif field_choice == '2':
                    new_category = input("Новая категория: ")
                    exp['category'] = new_category
                    print("✓ Категория обновлена")
                elif field_choice == '3':
                    new_description = input("Новое описание: ")
                    exp['description'] = new_description
                    print("✓ Описание обновлено")
                elif field_choice == '4':
                    print("Редактирование отменено")
                    return
                else:
                    print("Неверный выбор")
                    return

                save_expenses(expenses)
                print("\n✓ Расход успешно обновлен")
                return

        print(" Расход с таким ID не найден")
    except ValueError:
        print(" Ошибка: Введите корректные данные")
    except Exception as e:
        print(f" Ошибка: {e}")