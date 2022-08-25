# METHOD RESOLUTION ORDER YANG MANA MEMILIKI HUBUNGAN DENGAN MULTIPLE INHERITANCE 

class A:
    def _showA(self):
        PRINT("SHOW A")

class B:
     def _showB(self):
        PRINT("SHOW B")

# method resolution order
class C(A, B):
    def showC(self):
        print("ini show c")

objek = C()
objek.show()
# help(objek)