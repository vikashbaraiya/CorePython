str = input("enter any string = ")
s = input("enter which character you count =")
count = 0
for i in str:
    if i==s:
      count+=1
print("count = ",count)
