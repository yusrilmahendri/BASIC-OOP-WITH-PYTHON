# class abstak adalah blueprint from class 
# memaksa class untuk imlementasi methodnya 

#membuat class abstrak 
# abc sama abstrak base class 

from abc import ABC, abstractmethod

class Button(ABC):
    #DECERATOR 
    @abstractmethod
    def click():
       pass 

class push(Button):
    def click(self):
            print("ini adalah button click!")

tombol1 = push()
tombol1.click()