class Planet():
    counter=0
    def __init__(self,name,radius,mass,distance,planet_type):
        self.name=name
        self.radius=radius
        self.mass=mass
        self.distance=distance
        self.type=planet_type
        self.id=Planet.counter
        print(f"Создание планеты с ID: {self.id}")
        Planet.counter+=1

    def __str__(self):
        output='Планета '+self.name+'\n'+'Радиус '+str(self.radius)+'\n'+'Масса '+str(self.mass)+'\n'+'Расстояние до солнца '+str(self.distance)+'\n'+'Тип планеты '+str(self.type)+'\n'
        return output
    
    def __repr__(self):
        return (f"Planet(name='{self.name}',radius={self.radius}, "
                f"mass={self.mass},distance={self.distance}, "
                f"type='{self.planet_type}',id={self.id})")
    
    def __copy__(self):
        return Planet(self.name,self.radius,self.mass,self.distance,self.type)
    
    def __del__(self):
        print(f'Удаление планеты с ID: {self.id}')

    def __eq__(self, other):
        if not isinstance(other, Planet):
            return False
        return self.name == other.name
    
    def __ne__(self, other):
        if not isinstance(other, Planet):
            return True
        return self.name != other.name


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
        return self.type >= other.type
    def to_string(self):
        return f'{self.id};{self.name};{self.radius};{self.mass};{self.distance};{self.type}'


