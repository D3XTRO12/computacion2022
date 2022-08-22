num = int(input("Ingrese un entero: "))

def closer_100 (num):
    result = False
    z = abs(num)
    if z in range (0, 10):
        result = True
        return result
    if z in range (10, 100):
        result = True
        return result
    if z in range (100, 200):
        result = True
        return result
    

print(closer_100(num))
