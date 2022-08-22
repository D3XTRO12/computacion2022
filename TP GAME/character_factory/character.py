class Character():
    
    def __init__(self, name, age, strength, agility, health, class_type):
        self.name = name
        self.age = age
        self.__strength = strength
        self.__agility = agility
        self.__health = health
        self.type = class_type #SOLO 3 MAX

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_strength(self, strength):
        self.__strength = strength
    
    def set_agility(self, agility):
        self.__agility = agility
    
    def set_health(self, health):
        self.__health = health
    
    def set_type(self, class_type):
        self.type = class_type

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def get_strength(self):
        return self.__strength
    
    def get_agility(self):
        return self.__agility
    
    def get_health(self):
        return self.__health

    def get_type(self):
        return self.type
        
    def atack(self):
        pass

    def defense(self):
        pass

    def increase_atribute(self):
        pass

    