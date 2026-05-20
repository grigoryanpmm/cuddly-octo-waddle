import planet_menu
import employee_menu

def main():
    while True:
        choice = input("С каким классом мы будем работать ?(Planet,Employee): ")
        if choice == "Planet":
            planet_menu.menu()
            return
        elif choice == "Employee":
            employee_menu.menu()
            return
        else:
            print("Введите нужный класс")
if __name__ == '__main__':
    main()
