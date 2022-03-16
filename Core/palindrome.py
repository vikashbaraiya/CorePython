n = int(input("enter a number = "))
a = n
rev = 0
while(n>0):
      r = n%10
      rev = rev*10+r
      n = n // 10

if(rev==a):
    print("given no is palindrome")
else:
    print("number is not")
