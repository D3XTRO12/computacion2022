class LineExpresion:

    def __init__(self, archivo_name, oracion) -> None:
        self.archivo_name = archivo_name
        self.oracion = oracion

    
    def denotacion_search(self):
        for i, linea in enumerate(self.archivo_name.readlines(), 1):
            if self.oracion in linea:
                print(f"La palabra ingresada: {self.oracion}\nEsta denotada en la linea: {i}\n")

filename = input("Ingrese el nombre del archivo a denotar: ")
oracion = input("Denote la oracion que desea buscar: ")
with open(filename, 'r') as archivo:
    denotacion = LineExpresion(archivo, oracion)
    denotacion.denotacion_search()
