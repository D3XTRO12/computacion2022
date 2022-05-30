class LinesSelection:

    def __init__(self, cantidad_lineas, file_name):
        self.cantidad_lineas = cantidad_lineas
        self.file_name = file_name

    def lines_selection(self):
        for i in range(self.cantidad_lineas):
            line = self.file_name.readline()
            print(line, end='')


filename = input('Ingrese el nombre de archivo: ')
cant_lineas = int(input('Ingrese la cantidad de líneas a leer: '))
with open(filename, 'r') as archive:
    seleccion = LinesSelection(cant_lineas, archive)
    seleccion.lines_selection()