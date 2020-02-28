soma = 0
num = int (input ("Provide a number: "))
for number in range(1,num+1):
    if num%number==0:
        soma += number
print(soma)