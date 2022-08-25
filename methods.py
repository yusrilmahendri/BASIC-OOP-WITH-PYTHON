#methods adalah fungsi dari class from insttance
class Hero:
    #class variabel 
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth,inputPower, inputArmor):
        #instance variabel 
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # METHOD TANPA RETURN (VOID FUNCTION)
    def siapa(self):
        print("nama saya dalah " + self.name)

    # method dengan argument 
    def healthUp(self, up):
        self.health += up 

    # method dengan return 
    def getHealth(self):
        return self.health

hero1 = Hero('snipe', 10, 5, 100)
print(hero1.__dict__)
hero1.siapa()

hero1.healthUp(10)
print(hero1)

print(hero1.getHealth())