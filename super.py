# super for inheritance 
class Hero:
    def __init__(self, name, health):
        self.name = name 
        self.health = health 

class Hero_i(Hero):
    def __init__(self, name):
      # super cara 1 
      super().__init__(name, 100)

class hero_s(Hero):
    def __init__(self, name):
        super().__init__(name, 200)

lina = Hero_i('lina')
aku = hero_s('akui')
print(lina.name, " ", lina.health)
print(aku.name, " ", aku.health)

