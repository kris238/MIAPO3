from functions import add_expense
def main():
    print("=== СИСТЕМА УЧЕТА РАСХОДОВ ===")
    while True:
        print("\n1. Добавить расход")
        print("2. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            print("До свидания!")
            break
        else:
            print("Неверный выбор")
if __name__ == "__main__":
    main()