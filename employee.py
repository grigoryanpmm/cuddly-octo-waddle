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

    def __str__(self):
        output='Имя '+self.name+'\n'+'Должность '+self.position+'\n'+'Отдел '+self.section+'\n'+'Зарплата '+self.salary+'\n'+'Дата приема '+self.appointment+'\n'
        return output
    
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
        return f'{self.id};{self.name};{self.position};{self.section};{self.salary};{self.appointment}'
    
