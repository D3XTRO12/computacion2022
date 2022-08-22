class CamposDelimiter:

    def __init__(self, archivo_name, separador) -> None:
        self.archivo_name = archivo_name
        self.separador = separador

    def agregar_delimitador(self):
        leer = ' '.join(self.archivo_name)
        lista = leer.split(" ")
        leer_nuevo = self.separador.join(lista)
        print(leer_nuevo)

file_name = input("Ingrese el archivo:")
separador = input("Ingrese el separador que desea utilizar: ")
with open(file_name, 'r') as archivo:
    delimitar = CamposDelimiter(archivo, separador)
    delimitar.agregar_delimitador()