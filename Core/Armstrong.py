n = int(input("enter a number = "))
a = n
sum = 0
while(n>0):
      r = n%10
      rem = r*r*r
      sum = sum+rem
      n = n // 10

if(sum==a):
    print("given no is armstrong")
else:
    print("number is not")
