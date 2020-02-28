num_orig = int (input ("Please provide an integer: "))
num = num_orig
numero = 0
resultado = 0
while num > 0:
    numero = num%10
    num = num // 10
    resultado = resultado*10 + numero
if resultado == num_orig:
    result = "%d is a palindrome." %(num_orig)
else:
    result = "%d is not a palindrome." %(num_orig)
print(result)