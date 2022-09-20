import string
def bingo(array):
    numeros_a_letras = dict(zip(range(1, 27), string.ascii_uppercase))
    lista = []
    for i in array:
        lista.append(numeros_a_letras[i])
    if "B" in lista:
        if "I" in lista:
            if "N" in lista:
                if "G" in lista:
                    if "O" in lista:
                        return "WIN"
    else:
        return "LOSE"