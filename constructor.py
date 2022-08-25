# has magic keyword, def, __init__, self

class Hero:
    # cara ini akan berguna if menaruh argument 
    def __init__(self, x, inputName):
        self.name = inputName
        print("Hallo", x)
hero1 = Hero(10, "sniper")
print(hero1.name)
