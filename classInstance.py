# CLASS 

class Hero:
    #class variabel 
    jumlah = 0

    def __init__(self,inputName, inputHealith, inputPower, inputArmor):
        #INSTANCE VARIABEL 
        self.name = inputName
        self.healith = inputHealith
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah = 1
    
    # method tanpa argumen
    def siapa(self):
        print("nama adalaha" + self.name)

    #method dengan argumen 
    def healthUp(self, up):
        self.health += up
    
    # method dengan return 
    def getHealth(self):
        return self.health

hero1 = Hero("sniper", 100, 10, 4)
print(hero1)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())