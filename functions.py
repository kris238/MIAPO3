from пмпм import load_expenses, save_expenses


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

        print("❌ Расход с таким ID не найден")

    except ValueError:
        print("❌ Ошибка: Введите корректные данные")
    except Exception as e:
        print(f"❌ Ошибка: {e}")