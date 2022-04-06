from abc import ABC,abstractmethod


class Shape(ABC):
    def __init__(self, c,b):
        self.__color = c
        self.__borderWidth = b
    @abstractmethod
    def area(self):
        pass

    def getcolor(self):
        return self.__color

    def getBorderWidth(self):
        return self.__borderWidth
    def sum(self):
        pass

    def __str__(self):
        return self.__color



