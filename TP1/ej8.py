
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
negativa1 = False
negativa2 = True

def pos_negativa(num1, num2, negativa):
    if num1 > 0 and num2 < 0 and negativa == False:
        return print("True")
    if  num1 < 0 and num2 > 0 and negativa == False:
        return print("True")
    if num1 < 0 and num2 < 0 and negativa == True:
        return print("True")
    else:
        return print("False")


pos_negativa(num1, num2, negativa2)
