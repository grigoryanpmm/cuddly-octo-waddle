from planet import Planet

planets_list=[]

'''
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
            print('Название планеты должно быть строковым значением')
            continue
        print("Текстовое значение не может быть пустым")
'''

def add_planet():
    name=input('Введите название планеты: ')
    radius = input('Введите радиус планеты в километрах: ')
    mass = input('Введите массу планеты в килограммах: ')
    distance = input('Введите расстояние от планеты до Солнца в километрах: ')
    pl_type = input('Введите тип планеты: ')
    planet=Planet(name,radius,mass,distance,pl_type)
    planets_list.append(planet)
    print(f'Планета {name} с ID {planet.id} добавлена в БД')

def delete_planet():
    idd=input('Введите ID планеты для удаления: ')
    for planet in planets_list:
        if str(planet.id) == idd:
            planets_list.remove(planet)
            print("Планета удалена из БД")
            return
    print("Введенного ID нет в БД")
def edit_planet():
    idd=input('Введите ID планеты для изменения параметров: ')
    for planet in planets_list:
        if str(planet.id)==idd:
            print('Введите новые данные планеты:')
            planet.name=input('Название: ')
            planet.radius=input('Радиус в километрах:')
            planet.mass=input('Масса в килограммах:')
            planet.distance=input('Расстояние от планеты до Солнца в километрах:')
            planet.pl_type=input('Тип планеты: ')
            print('Планета изменена')
            return
    print("Такого ID нет в базе данных.")

def conclusion():
    if not (planets_list):
        print('В БД ничего нет')
    else:
        for planet in planets_list:
            print(planet)

            
def save_to_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for p in planets_list:
            f.write(p.to_string() + "\n")
    print("Данные сохранены в текстовый файл.")
    
    

def load_from_file(file_name):
    with open(file_name,'r',encoding='UTF-8') as f:
        for s in f:
            if not s.strip():
                continue
            parts=s.strip().split(';')
            planet=Planet(parts[0],float(parts[1]),float(parts[2]),float(parts[3]),parts[4])
            planets_list.append(planet)
        print('Данные успешно загружены!')
    return planets_list


def sort_planets():
    if not planets_list:
        print("В БД нет объектов")
        return
    print("Выберите по какому полю хотите отсортировать БД:")
    print("1 если сортировка по расстоянию до Солнца")
    print("2 если сортировка по радиусу")
    print("3 если сортировка по массе")
    choice = input("Выбор: ")
    n = len(planets_list)
    for i in range(n):
        for j in range(n - i - 1):
            if choice=='1':
                if planets_list[j+1]<planets_list[j]:
                    planets_list[j], planets_list[j + 1] = planets_list[j + 1], planets_list[j]
            elif choice=='2':
                if planets_list[j]>planets_list[j+1]:
                    planets_list[j], planets_list[j + 1] = planets_list[j + 1], planets_list[j]
            elif choice=='3':
                if not planets_list[j]<=planets_list[j+1]:
                    planets_list[j], planets_list[j + 1] = planets_list[j + 1], planets_list[j]
            else:
                print("Выбор неккоректный")
                return
    print("Планеты успешно отсортированы")





def menu():
    while True:
        print('Выберите нужную опцию:')
        print('1 - чтение из БД (текстового документа)')
        print('2 - запись в БД (текстовый документ)')
        print('3 - сортировка временной БД по выбранному полю')
        print('4 - добавление нового объекта в временную БД')
        print('5 - редактирование объекта в временной БД')
        print('6 - удаление объекта из временной БД')
        print('7 -вывод БД на экран ')
        print('8 - завершение работы')
        choice=input('Выбор: ')
        if choice=='1':
            planets_list=[]
            file_name=input('Введите имя файла: ')
            load_from_file(file_name)
        elif choice=='2':
            file_name=input('Введите имя файла: ')
            save_to_file(file_name)
        elif choice=='3':
            sort_planets()
        elif choice=='4':
            add_planet()
        elif choice=='5':
            edit_planet()   
        elif choice=='6':
            delete_planet()
        elif choice=='7':
            conclusion()
        elif choice=='8':
            choice_2=input('Будете переносить данные из временой БД в текстовый документ? Введите "Да" или "Нет": ')
            if choice_2=='Да':
                file_name=input('Введите имя файла: ')
                save_to_file(file_name)
                print('Выход')
            elif choice_2!='Нет':
                print('Вы ввели неккоректный ответ. Данные не будут перенесены.')
            break
        else:
            print('Ввод неккоректный')
