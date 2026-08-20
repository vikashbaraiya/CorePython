a = int(input("enter a number = "))
b = int(input("enter a number = "))
print("1 for addition")
print("2 for substaction")
print("3 for multiplication")
print("4 for Division")
print("5 for Modulus")
print(" 6 for fully Divisible")
n = int(input("enter your choice= "))
mult1=0
div1=0
mod1=0
int_div1=0
sum2=0
c=0


if n==1:
    try:

        sum=a+b
        if(a==10):
            if(b==10):
                c=25
                sum2=a+b
                raise Exception('this is great', sum2 + c != 0)
    except:
        print("Addition = ",sum2+c)
    else:
        print("Addition ",sum)
elif n==2:
    try:

        min = a - b
        if (a == 50):
            if (b == 20):
                c = 10
                min2 = a - b
                raise Exception('this is great', min2 + c != 0)
    except:
        print("Minus",sum2 + c)
    else:
        print('Minus = ',min)

elif n ==3:
    try:

        mult = a * b
        if (a == 5):
            if (b == 5):
                c = 10
                mult1 = a * b
                raise Exception('this is great', mult1 + c != 0)
    except:
        print("Multiply",mult1 + c)
    else:
        print('Multiply = ',mult)

elif n==4:
    try:

        div = a / b
        if (a == 20):
            if (b == 5):
                c = 1
                div1 = a / b
                raise Exception('this is great', div1 + c != 0)
    except:
        print("Division",div1 + c)
    else:
        print('Division = ',div)

elif n==5:
    try:

        mod = a % b
        if (a == 20):
            if (b == 3):
                c = 1
                mod1 = a / b
                raise Exception('this is great', mod1 + c != 0)
    except:
        print("Modulas =", mod1 + c)
    else:
        print('Modulas = ', mod)

elif n==6:
    try:

        int_div = a // b
        if (a == 20):
            if (b == 3):
                c = 2
                int_div1 = a / b
                raise Exception('this is great', int_div1 + c != 0)

    except:
        print("Modulas =", int_div1 + c)
    else:
        print('Modulas = ', int_div)
