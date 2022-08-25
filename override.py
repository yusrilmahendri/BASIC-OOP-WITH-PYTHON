# overide method yang ada di super class 
# overring bisa diaktakan menimpan fungsi yang ada dalam subclass

class Hero:
    def __init__(self, name, health):
        self.name = name 
        self.health = health 
        
        # overide
    def showInfo(self):
        print("show info di class")
        print("{} health: {}". format(
            self.name, 
            self.health
            )
        )

class Hero_i(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
    
    # overide
     def showInfo(self):
        print("show info di sub class")
        print("{}tipe: intellegencae, health: {}". format(
            self.name, 
            self.health
            )
        )

class Hero_s(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

lina = Hero_i('lina')
print(lina)
si = Hero_s('ALEX')

lina.showInfo()
si.showInfo()