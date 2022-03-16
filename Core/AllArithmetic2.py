a = int(input("enter a = "))
b = int(input("enter b = "))
n = int(input("enter your choice"))
if n ==1:
    def sum(a,b):
        c = a+b
        return c
    print(sum(a,b))
elif n ==2:
    def sub(a,b):
        c = a-b
        return c
    print(sub(a,b))
elif n==2:
    def mult(a,b):
        c = a*b
        return c
    print(mult(a,b))
elif n==4:
    def div(a,b):
        c = a/b
        return c
    print(div(a,b))
elif n==5:
    def mod(a,b):
        c=a%b
        return c
    print(mod(a,b))