
from datetime import date
class Employee():
    counter=0
    def __init__(self,name,position,section,salary,appointment):
        self.name=name
        self.position=position
        self.section=section
        self.salary=salary
        self.appointment=appointment
        self.id=Employee.counter
        print(f"Создание сотрудника с ID: {self.id}")
        Employee.counter+=1


    @property
    def name(self):
        return self.__name
            
    @name.setter
    def name(self, value):
        if value.isdigit() or len(value) == 0:
            raise ValueError("Введите строковое значение, длина которого больше 0.")
        self.__name = value

    @property
    def position(self):
        return self.__position       

    @position.setter    
    def position(self, value):
        if value.isdigit() or len(value) == 0:
            raise ValueError("Введите строковое значение, длина которого больше 0.")
        self.__position = value
        

    @property
    def section(self):
        return self.__section              

    @section.setter
    def section(self,value):
        if value.isdigit() or len(value) == 0:
            raise ValueError("Введите строковое значение, длина которого больше 0.")
        self.__section = value
    @property
    def salary(self):
        return self.__salary      

    @salary.setter    
    def salary(self,value):
        if not value.isdigit() or int(value)<=0:
            raise ValueError('вод должен быть числом большим чем 0')
        self.__salary=int(value)

    @property
    def appointment(self):
        return self.__appointment       

    @appointment.setter    
    def appointment(self, value):
        parts=value.split()
        if not(len(parts)==3 or all(part.isdigit() for part in parts)):
            raise ValueError('"Ввод должен состоять из 3 числовых значений. Месяц- число от 1 до 12, день- число от 1 до 365."')
        self.__appointment=date(int(parts[0]),int(parts[1]),int(parts[2]))

    

    def __str__(self):
        return (f"Имя {self.name} | Должность {self.position} | Отдел {self.section} | Зарплата в рублях {self.salary} | Дата приема {self.appointment} | id {self.id}")
    
    def __repr__(self):
        return (f"Employee(name='{self.name}',position={self.position}, "
                f"section={self.section},salary={self.salary}, "
                f"appointment='{self.appointment}',id={self.id})")
    
    def __copy__(self):
        return Employee(self.name,self.position,self.section,self.salary,self.appointment)
    
    def __del__(self):
        print(f'Удаление сотрудника с ID: {self.id}')

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return False
        return self.name == other.name
    
    def __ne__(self, other):
        if not isinstance(other, Employee):
            return True
        return self.name > other.name


    def __lt__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.salary < other.salary


    def __gt__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.appointment >= other.appointment


    def __le__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.salary <= other.salary


    def __ge__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.appointment >= other.appointment
    def to_string(self):
        return f'{self.name};{self.position};{self.section};{self.salary};{self.appointment}'
    

