class ContenidoTxt:

    def __init__(self, archivo_name, numero_linea, numero_palabra, numero_caracter) -> None:
        self.archivo_name = archivo_name
        self.numero_lineas = numero_linea
        self.numero_palabras = numero_palabra
        self.numero_caracteres = numero_caracter

    def leer_contenido_de_archivo(self):
        for linea in self.archivo_name:
            palabras = linea.split()
            self.numero_lineas += 1
            self.numero_palabras += len(palabras)
            self.numero_caracteres += len(linea)

    def imprimir_contenido(self):
        print(f"El archivo contiene : {self.numero_lineas} lineas")
        print(f"El archivo contiene : {self.numero_palabras} palabras")
        print(f"El archivo contiene : {self.numero_caracteres} caracteres")

file_name = input("Ingresa el nombre del archivo:")

numero_lineas = 0
numero_palabras = 0
numero_caracteres = 0

with open(file_name, 'r') as archivo:
    lectura = ContenidoTxt(archivo, numero_lineas, numero_palabras, numero_caracteres)
    lectura.leer_contenido_de_archivo()
    lectura.imprimir_contenido()



