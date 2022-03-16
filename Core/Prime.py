n = int(input("enter any number = "))
if n>1:
    for i in range(2, n//2):
        if(n%i)==0:
            print("not prime")
            break
    else:
         print(n,"is prime")
else:
        print('not prime')


