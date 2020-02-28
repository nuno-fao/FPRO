n1 = int(input("Please provide a number: "))
n2 = int(input("Please provide another: "))
x=0
while True:
    if (n2 // 10**x < 10):
        break
    x+=1
result = n1*(10**(x+1)) + n2
print (result)