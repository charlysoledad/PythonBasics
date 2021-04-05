'''
2 underscore to declarate private variable '__variable'
'''
class Cars:
    def __init__(self,name, speed, color):
        self.__name = name
        self.__speed = speed
        self.__color = color
    
    def setName(self, new_name):
        self.__name = new_name

    def getName(self):
        return self.__name
    
    def setSpeed(self, new_speed):
        self.__speed = new_speed

    def getSpeed(self):
        return self.__speed
    
    def setColor(self, new_color):
        self.__color = new_color

    def getColor(self):
        return self.__color

ford = Cars("Ford",250,"green")
nissan = Cars("Nissan",200,"gray")
toyota = Cars("Toyota",300, "red")

ford.setSpeed(450)

print(ford.getSpeed())