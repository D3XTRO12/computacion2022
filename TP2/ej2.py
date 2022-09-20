import os, re

def renombrar(list_name):
  for nombre in list_name:
    nuevo_nombre = re.sub(r"\d","", nombre)
    print(f"{nombre} se renombrará como \n{nuevo_nombre}\n")
    os.chdir(r'/home/d3xtro/Documents/UM SEGUNDO AÑO/computacion/SecretKey')
    os.rename(nombre, nuevo_nombre)

list_name = os.listdir(r'/home/d3xtro/Documents/UM SEGUNDO AÑO/computacion/SecretKey')
print(list_name)
renombrar(list_name)