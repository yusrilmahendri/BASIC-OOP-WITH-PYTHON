class Hero:
    def __init__(self, name, health, armor):
        self.__name = name 
        self.__health = health 
        self.__armor = armor
        # self.info = "name {} : \n\thealth: {}".format(self.__name, self.__health) 
    # def getHealth(self):
    #     return self.__health

    #properti then method can di anggap variabel 
    # sama dengan getter keunggulannya otomatis update 
    @property
    def info(self):
        return "name {} : \n\thealth: {}". format(self.__name, self.__health) 
    
    # method cant create property 
    @property
    def armor(self):
        pass 

    # getter dan setter 
    @armor.getter 
    def armor(self):
        return self.__armor
    @armor.setter 
    def armor(self, input):
        self.__armor = input
    

sniper = Hero('sniper', 100 , 10)
print(sniper.info)

# contoh auto update 
sniper.name = "dadang"
print(sniper.info)
print(sniper.__dict__)

print("getter dan setter for armor")
print(sniper.armor)

# call setter 
sniper.armor = 50
print(sniper.armor)
print(sniper.__dict__)

print("delete armor")
del sniper.armor
print(sniper.__dict__)