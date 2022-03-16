n = int(input("number = "))
evensum   = 0
evenavg   = 0
evencount = 0
for i in range(2,n,2):
    evensum = evensum +i
    evencount+=1

evenavg = evensum//evencount
print("even = ",evenavg)
oddsum   = 0
oddcount = 0
oddavg   = 0
for j in range(1,n,2):
    oddsum = oddsum+j
    oddcount+=1
oddavg = oddsum//oddcount
print("odd = ",oddavg)
