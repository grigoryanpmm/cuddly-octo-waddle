from employee import Employee
from datetime import date

employees_list=[]


def correct_float(text):
    while True:
        try:
            inputt=float(input(text))
            if inputt<=0:
                print("Число должно быть больше 0")
                continue
            return inputt
        except ValueError:
            print("Введите число")
def correct_str(text):
     while True:
        inputt=input(text).strip()
        if inputt:
            if not inputt.isdigit():
                return inputt
            print('Ввод должен быть строковым значением')
            continue
        print("Текстовое значение не может быть пустым")
def correct_date(text):
     while True:
        inputt=input(text).strip()
        date_list=list(inputt.split())
        try:
            date_list=list(map(int,date_list))
            return date(date_list[0],date_list[1],date_list[2])
        except (ValueError,TypeError,IndexError):
            print("Ввод должен состоять из 3 числовых значений. Месяц- число от 1 до 12, день- число от 1 до 365.")

def save_to_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for p in employees_list:
            f.write(p.to_string() + "\n")
    print("Данные сохранены в текстовый файл.")
    
    

def load_from_file(file_name):
    with open(file_name,'r',encoding='UTF-8') as f:
        for s in f:
            if not s.strip():
                continue
            parts=s.strip().split(';')
            employee=Employee(parts[0],parts[1],parts[2],float(parts[3]),datetime.strptime(parts[4]))
            employees_list.append(employee)
        print('Данные успешно загружены!')
    return employees_list


def conclusion():
    if not (employees_list):
        print('В БД ничего нет')
    else:
        for employee in employees:
            print(employee)




def add_employee():
    name=correct_str('Введите ФИО сотрудника: ')
    position = correct_str('Введите должность сотрудника: ')
    section = correct_str('Введите отдел сотрудника: ')
    salary = correct_float('Введите зарплату сотрудника в рублях: ')
    appointment = correct_date('Введите дату приема сотрудника (перечислите год, месяц и день через пробел в формате 2024 5 26): ')
    employee=Employee(name,position,section,salary,appointment)
    employees_list.append(employee)
    print(f'Сотрудник {employee.name} с ID {employee.id} добавлен в БД')



def search():
    print('Выберите по какому критерию вы хотите найти сотрудника:')
    print('1 - поиск по ФИО сотрудника')
    print('2 - по зарплате сотрудника')
    print('3 - по дате приема сотрудника')

    choice=input('Выбор: ')
    found=False

    if choice=='1':
        name=correct_str('Введите ФИО сотрудника: ')

        for employee in employees_list:
            if employee.name.lower()==name.lower():
                print(employee)
                found=True

    elif choice=='2':
        salary=correct_float('Введите зарплату сотрудника в рублях: ')

        for employee in employees_list:
            if employee.salary==salary:
                print(employee)
                found=True
    elif choice=='3':
        salary=correct_date('Введите дату приема сотрудника (перечислите год, месяц и день через пробел в формате 2024 5 26): ')

        for employee in employees_list:
            if employee.salary==salary.lower():
                print(employee)
                found=True
    else:
        print("Ввод неккоректен.")
        return
    if not found:
        print('Сотрудника с введенным критерием в БД нет.')    

def delete_employee():
    idd=input('Введите ID сотрудника для удаления: ')
    for employee in employees_list:
        if str(employee.id) == idd:
            employees_list.remove(employee)
            print("Сотрудник удален из БД")
            return
    print("Введенного ID нет в БД")
def edit_employee():
    idd=input('Введите ID сотрудника для изменения параметров: ')
    for employee in employees_list:
        if str(employee.id)==idd:
            print('Введите новые данные отрудника:')
            planet.name=correct_str('ФИО: ')
            planet.position=correct_str('Должность сотрудника: ')
            planet.section=correct_str('Отдел сотрудника: ')
            planet.salary=correct_float('Зарплата сотрудника в рублях: ')
            planet.appointment=correct_date('Дата приема сотрудника (перечислите год, месяц и день через пробел в формате 2024 5 26) : ')
            print('Сотрудник изменен')
            return
    print("Такого ID нет в базе данных.")



def sort_employees():
    if not employees_list:
        print("В БД нет объектов")
        return
    print("Выберите по какому полю хотите отсортировать БД:")
    print("1 если сортировка по ФИО сотрудника")
    print("2 если сортировка по зарплате сотрудника")
    print("3 если сортировка по дате приема сотрудника")
    choice = input("Выбор: ")
    n = len(employees_list)
    for i in range(n):
        for j in range(n - i - 1):
            if choice=='1':
                if employees_list[j]!=employees_list[j+1]:
                    employees_list[j], employees_list[j + 1] = employees_list[j + 1], employees_list[j]
            elif choice=='2':
                if employees_list[j+1]<employees_list[j]:
                    employees_list[j], employees_list[j + 1] = employees_list[j + 1], employees_list[j]
            elif choice=='3':
                if not employees_list[j+1].appointment>=employees_list[j].appointment:
                    employees_list[j], employees_list[j + 1] = employees_list[j + 1], employees_list[j]
            else:
                print("Выбор неккоректный")
                return
    print("Сотрудники успешно отсортированы")



def export_to_csv():
    file_name=input('Введите название файла для экспорта в CSV: ')
    headers=['id','name','position','section','salary','appointment']
    if not file_name.endswith('.csv'):
        file_name+='.csv'
    with open(file_name, 'w', encoding='UTF-8') as file:
        writer=csv.writer(file,delimiter=';')
        writer.writerow(headers)
        writer.writerows(employees_list)
    print(f"Данные упешно экспортированы в {file_name}")



def menu():
    while True:
        print('Выберите нужную опцию:')
        print('1 - Загрузка БД из файла')
        print('2 - Сохранение БД в файл')
        print('3 - Просмотр всех записей ')
        print('4 - Добавление нового сотрудника в временную БД')
        print('5 - Поиск сотрудника по критерию')
        print('6 - Редактирование сотрудника БД')
        print('7 -Удаление сотрудника из временной БД ')
        print('8 - Сортировка БД')
        print('9 -Экспорт в CSV ')
        print('10 - Завершение работы')
        choice=input('Выбор: ')
        if choice=='1':
            employees_list=[]
            file_name=input('Введите имя файла: ')
            load_from_file(file_name)
        elif choice=='2':
            file_name=input('Введите имя файла: ')
            save_to_file(file_name)
        elif choice=='3':
            conclusion()
        elif choice=='4':
            add_employee()
        elif choice=='5':
            search()   
        elif choice=='6':
            edit_employee()
        elif choice=='7':
            delete_employee()
        elif choice=='8':
            sort_employees()
        elif choice=='9':
            export_to_csv()
        elif choice=='10':
            choice_2=input('Будете переносить данные из временой БД в текстовый документ? Введите "Да" или "Нет": ')
            if choice_2=='Да':
                export_to_csv()
                print('Выход')
            elif choice_2!='Нет':
                print('Вы ввели неккоректный ответ. Данные не будут перенесены.')
            break
            
        else:
            print('Ввод неккоректный')


