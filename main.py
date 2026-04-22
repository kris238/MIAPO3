from functions import add_expense, view_expenses, delete_expense

def main():
    print("=== СИСТЕМА УЧЕТА РАСХОДОВ ===")
    while True:
        print("\n1. Добавить расход")
        print("2. Просмотреть расходы")
        print("3. Удалить расход")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()