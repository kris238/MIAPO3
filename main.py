from functions import add_expense, view_expenses


def main():
    print("=== СИСТЕМА УЧЕТА РАСХОДОВ ===")
    while True:
        print("\n1. Добавить расход")
        print("2. Просмотреть расходы")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()