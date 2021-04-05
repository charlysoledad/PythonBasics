from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.__side = side
    
    def area(self):
        return self.__side * self.__side
    def perimeter(self):
        return self.__side * 4

# myShape = Shape() not can be used because is abstract

mySquare = Square(4)

print(mySquare.area())