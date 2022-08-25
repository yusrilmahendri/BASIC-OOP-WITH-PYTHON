# inheritance adalah pewarisan ialah sesuatu yang diwariskan wkwkwkwk ahhah canda bro 
# inheritance ini berlaku antar class ke class 
#  class 1 disebutkan sebagai super class sedangkan class 2 disebutkan subclass

class Hero:
    def __init__(self, name, health):
        self.name = name 
        self.health =health

# inheritance ambil dari super class 
# techies jadi punya hero dari class hero yang sduah diwariskan dari hero 
class Hero_interlligent(Hero):
    pass 

lina = Hero('lina', 100)
print(lina.name) 

techies = Hero_interlligent('techies', 50)
print(techies.name)
# print(help(techies))