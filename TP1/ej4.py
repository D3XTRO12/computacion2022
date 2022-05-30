num = int(input("Ingrese un numero: "))

def dif_21(num):
    result = 0
    x = 21
    if num < x:
        result = x - num
    elif num > x:
        result = (num - x) * 2
    return result

print("El resultado de la diferencia entre el numero ingresado y 21 es:", dif_21(num))