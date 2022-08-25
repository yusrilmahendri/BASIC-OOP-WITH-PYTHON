class Hero:
    # class variabel
    jumlah = 0

    def __init__(self, name, health):
        self.name = name 
        self.health = health

    # variabel private (insatnce) bersifat private 
    # in python not idintifier variabel, akan tetapi cant conversi 
    # how cant create variabel private 
        self.__private = "private"
        
    #protected hampir the same public akan tetapi cant acces in only class
    self.protected = "protected"

lina = Hero("lina", 100)

# fleksibilitas from python if insert variabel 
lina.private = "testing"
print(lina.__dict__)

# call 
print(lina.private)