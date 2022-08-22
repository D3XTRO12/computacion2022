num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero: "))

def make10 (num1, num2):
    z = 0
    result = False
    if num1 == 10:
        result = True
    if num2 == 10:
        result = True
    z = num1 + num2
    if z == 10:
        result = True
    return result

print(make10(num1, num2))
