# MULTIPLE INHERITANCE adalah ia bisa mendaaptka dari banyak class

class A:
    def method_A(self):
        print("ini methoda a")

class B:
    def method_B(self):
        print("ini method b")

class Sesuatu(A, B):
    pass 

objek = Sesuatu()

objek.method_A() 
objek.method_B() 
