
class Mangga():
    # magic method adalah keyword yang sudah ada keword di python yang mana akan digunakan kembali
    def __init__(self, nama, jumlah):
        self.nama = nama 
        self.jumlah = jumlah 
    
    # magic reper from method
    def __repr__(self):
        return 'ini adalah __repr__'

    # magic method str 
    def __str__(self):
        return 'ini magic method str'

    #magic method__add__ 
    def __add__(self, objek):
        return self.jumlah + objek.jumlah

    # if dictinoray wajib nambah property 
    def __dict__(self):
        return "objek ini has nama dan jumlah"

belanja1 = Mangga("arumanis", 100)
belanja2 = Mangga("arum", 10)
print(belanja1.nama)
print(repr(belanja1))
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)