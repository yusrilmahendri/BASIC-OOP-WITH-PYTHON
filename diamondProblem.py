# diamond problem 
# berhubungan dengan 
# METHOD RESOLUTION 

class A:
    def _showA(self):
        PRINT("SHOW A")

class B(A):
     def _showB(self):
        PRINT("SHOW B")

# method resolution order
class C(A):
    def showC(self):
        print("ini show c")

class D(B,C):
    pass         

objek = D()
objek.show()