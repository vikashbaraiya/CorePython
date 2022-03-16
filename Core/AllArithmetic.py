a = int(input("enter a number"))
b = int(input("enter a number"))
print("1 for addition")
print("2 for substaction")
print("3 for multiplication")
print("4 for Division")
print("5 for Modulus")
n = int(input("enter your choice"))

if n==1:
    sum = a + b
    print("sum =",sum)
elif n==2:
    sub = a - b
    print("sub =",sub)
elif n ==3:
    mult = a*b
    print("mult =",mult)
elif n==4:
    div = a/b
    print("div =",div)
elif n==5:
    mod = a%b
    print("mod =",mod)
elif n==6:
    div2 = a//b
    print("div2 =",div2)	
