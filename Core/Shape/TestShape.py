from Circle import *
from Triangle import *
from Rectangle import *
n = int(input("enter your choice"))

tri_obj = Triangle(base,height)
c = tri_obj.area()


cir_obj = Circle(r)
d = cir_obj.area()

rec_obj = Rectangle(lenght,width)
e = rec_obj.area()
f =c+d+e

print('Total sum of area is =',f)
print('Area of Triangle is : ',tri_obj.area())
print('Area of Circle is : ', cir_obj.area())
print('Area of Rectangle is : ',rec_obj.area())

