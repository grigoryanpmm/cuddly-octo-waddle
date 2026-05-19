class Planet():
    counter=0
    def __init__(self,name,radius,mass,distance,pl_type):
        self.name=name
        self.radius=radius
        self.mass=mass
        self.distance=distance
        self.pl_type=pl_type
        self.id=Planet.counter
        print(f"Создание планеты с ID: {self.id}")
        Planet.counter+=1


    @property
    def name(self):
        return self.__name
            
    @name.setter
    def name(self, value):
        if value.isdigit() or len(value) == 0:
            raise ValueError("Введите строковое значение, длина которого больше 0.")
        self.__name = value

    @property
    def radius(self):
        return self.__radius              

    @radius.setter
    def radius(self,value):
        if not value.isdigit() or int(value)<=0:
            raise ValueError('Ввод должен быть числом большим чем 0')
        self.__radius=int(value)

    @property
    def mass(self):
        return self.__mass      

    @mass.setter    
    def mass(self,value):
        if not value.isdigit() or int(value)<=0:
            raise ValueError('Число должно быть больше 0')
        self.__mass=int(value)

    @property
    def pl_type(self):
        return self.__pl_type       

    @pl_type.setter    
    def pl_type(self, value):
        if value.isdigit() or len(value) == 0:
            raise ValueError("Введите строковое значение, длина которого больше 0.")
        self.__pl_type = value
   
    def __str__(self):
        return (f"Планета {self.name} | Радиус {self.radius}"
            f"Масса {self.mass} | Расстояние до солнца в км {self.distance} "
            f"Тип {self.pl_type} | id {self.id}")
    
    def __repr__(self):
        return (f"Planet(name='{self.name}',radius={self.radius}, "
                f"mass={self.mass},distance={self.distance}, "
                f"pl_type='{self.planet_type}',id={self.id})")
    
    def __copy__(self):
        return Planet(self.name,self.radius,self.mass,self.distance,self.pl_type)
    
    def __del__(self):
        print(f'Удаление планеты с ID: {self.id}')

    def __eq__(self, other):
        if not isinstance(other, Planet):
            return False
        return self.name == other.name
    
    def __ne__(self, other):
        if not isinstance(other, Planet):
            return True
        return self.name > other.name


    def __lt__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented
        return self.distance < other.distance


    def __gt__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented
        return self.radius > other.radius


    def __le__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented
        return self.mass <= other.mass


    def __ge__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented
        return self.pl_type >= other.pl_type
    def to_string(self):
        return f'{self.id};{self.name};{self.radius};{self.mass};{self.distance};{self.pl_type}'


