class LineasSelection:

    def __init__(self, cantidad_lineas, archivo_name) -> None:
        self.cantidad_lineas = cantidad_lineas
        self.archivo_name = archivo_name

    def lines_selection(self):
        for i in range(self.cantidad_lineas):
            linea = self.archivo_name.readline()
            print(linea, end='')


filename = input('Ingrese el nombre de archivo: ')
cant_lineas = int(input('Ingrese la cantidad de líneas a leer: '))
with open(filename, 'r') as archivo:
    seleccion = LineasSelection(cant_lineas, archivo)
    seleccion.lines_selection()