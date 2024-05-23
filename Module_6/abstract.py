#abstract base class
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name) ->None:
        self.category = 'Monkey'
        self.name = name
        super().__init__()
    def eat(self):
        print('Eatinggg')

layka = Monkey('Lucky')
layka.eat()