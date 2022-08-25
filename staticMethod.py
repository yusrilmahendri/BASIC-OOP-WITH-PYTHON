#private class variabel 

class Hero:
    __jumlah = 0

def __init__(self, name):
    self.__name = name 
    Hero__jumlah += 1 

    # getter 
    # method ini only berlaku for objek 
    def getJumlah(self):
        return Hero.__jumlah
    # not berlaku for objek akan tetapi berlaku for class 
    def getJumlah1():
        return Hero.__jumlah
    
    # static method (decetrator) merupakan solusi for problem tersebut 
    # staic method akan nempel ke objek dan class
    # satatic method tidak bisa ambil argument
    @staticmethod
        def getJumlah2():
        return Hero.__jumlah

    # cara nempel ke class 
    # bisa ambil argument
    @classmethod
        def getJumlah3(cls):
            return cls.__jumlah


seniper = Hero('sniper')
print(Hero.getJumlah2())
rikimare = Hero('rikimaru')
print(sniper.getJumlah2())
drow = Hero('drowk')
print(sniper.getJumlah3())
