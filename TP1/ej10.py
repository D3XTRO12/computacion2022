str_chain = str(input("Ingrese una palabra: "))

n = int(input("Ingrese el indice de la cadena a eliminar: "))

def lost_index(str_chain, n):
    if 0 <= n < len(str_chain):
        str_new = str_chain.replace(str_chain[n], "")
        print(str_new)
    else:
        print("n no es un indice valido")

lost_index(str_chain, n)
