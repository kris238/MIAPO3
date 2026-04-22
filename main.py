from functions import add_expense, view_expenses, delete_expense, edit_expense

def main():
    print("=== СИСТЕМА УЧЕТА РАСХОДОВ v1.0 ===")
    while True:
        print("\n" + "=" * 40)
        print("ГЛАВНОЕ МЕНЮ")
        print("=" * 40)
        print("1. ➕ Добавить расход")
        print("2. 📋 Просмотреть расходы")
        print("3. 🗑️  Удалить расход")
        print("4. ✏️  Редактировать расход")
        print("5. 🚪 Выход")
        print("=" * 40)
        choice = input("Выберите действие (1-5): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            edit_expense()
        elif choice == '5':
            print("\n👋 До свидания! Хорошего дня!")
            break
        else:
            print("\n❌ Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()