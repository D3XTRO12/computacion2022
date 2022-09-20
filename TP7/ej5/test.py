def consecutive(array, a, b):
    lista = []
    for i in array:
       lista.append(i)
    if lista.index(a) > lista.index(b) or lista.index(a) < lista.index(b):
        return True
    else:
        return False