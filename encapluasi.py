# encapluasi syrat : cant create all variabel private, geeter dan setter
# getter for get variabel
# setter seeting variabel
class Hero:
    def __init__(self, name, health, attackPower):
        self.__name = name 
        self.__health = health 
        self.__attPower = attackPower

    #getter 
    def getName(self):
        return self.__name 
    
    def getHealth(self):
        return self.__health
    
    # SETTER 
    def serang(self, attack):
        self.__health -= attack

    def setAttPower(self, nilai):
        self.__attPower = nilai

earthShaker = Hero(" earth shaker", 50, 5)
# print(earthShaker.__dict__)
print(earthShaker.getName())
print(earthShaker.getHealth())
print(earthShaker.serang(5))
print(earthShaker.getHealth())