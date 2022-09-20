file = open("segundo archivo.txt", "a")
file.write("\nhola de nuevo")
file.close()

file = open("segundo archivo.txt", "r")
print(f"la lista anterior del archivo es: \n{file.readlines()}\n")

with open("segundo archivo.txt", "r") as archivo:
    lista = [linea.rstrip() for linea in archivo]
    lista.pop(0)

print(f"La nueva lista es: \n{lista}")