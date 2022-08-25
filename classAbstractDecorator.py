from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def __init__(self, link):
        self.link = link                    

    def lin(self):
        pass              
    
    @property
    @abstractmethod
    def lin(self):
        pass 

class PushButton(Button):
    
    def click(self):
      print("go to : {}". format(self.link))

    # implementasi link 
    @Button.link.setter 
    def link(self):
        #  atribut private 
        self.__link = input
    
    @link.getter  
    def link(self):
        return self.__link

tombol1 = PushButton()
tombol1 =PushButton("yusril.com")
tombol1.click()