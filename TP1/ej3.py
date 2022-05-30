num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

def add_double (num1, num2):
    result = 0
    if num1 != num2:
        result = num1 + num2
    elif num1 == num2:
        result = (num1 + num2) * 2
    return result
print("El resultado de la operacion es: ", add_double(num1, num2))