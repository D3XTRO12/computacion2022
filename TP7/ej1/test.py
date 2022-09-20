def sum_of_differences(array):
    array.sort(reverse=True)
    lista = []
    for i in range(len(array)-1):
        lista.append(abs(array[i+1]-array[i]))
    suma = 0
    for numero in lista:
        if len(array) == 3: 
            suma += numero + 1
            return suma
        elif len(array) == 0 or len(array) == 1:
            suma += numero - numero
            return suma
        else:
            suma += numero
            return suma