hora = int(input("Ingrese la hora actual: "))
if hora > 24:
    print("HORA NO VALIDA")
loro_habla = str(input("Esta el loro Hablando?: "))

speak = False
if loro_habla == "si":
    speak = True
elif loro_habla == "no":
    speak = False
def truble_loro(hora, loro_habla):
    z = False
    if hora > 7 & hora < 20  & speak == True:
        z = False
    elif hora > 7 & hora < 20 & speak == False:
        z = False
    elif hora > 0 & hora < 7 & speak == True:
        z = True
    elif hora > 20 & hora < 23 & speak == True:
        z = True
    elif hora > 20 & hora < 23 & speak == False:
        z = False
    
    
    return z
if truble_loro(hora, loro_habla) == False:
    print("We aren't in trouble")
elif truble_loro(hora, loro_habla) == True:
    print("We're in trouble")