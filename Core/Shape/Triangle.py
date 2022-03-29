from Shape import *
base =int(input('enter base = '))
height = int(input('enter height = '))
class Triangle(Shape):
    def __init__(self,base, height,c='',b=0):
        self.__base = base
        self.__height =height
        super(Triangle,self).__init__(c,b)

    def area(self):
       return (self.__base*self.__height)/2
    