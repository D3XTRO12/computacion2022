from itertools import islice

class ArchiveLine:

    def __init__(self, archivo, cantidad_de_lineas):
        self.archivo = archivo
        self.cantidad_de_lineas = cantidad_de_lineas


    def set_read(self, read):
        self.archivo = read
    

    def get_read(self):
        for lineas in islice(self.archivo, self.cantidad_de_lineas):
            print(lineas)
        
nombre_archivo = open(r"/home/d3xtro/Documents/computacion/TP2-P2/archivos txt/ej2.txt", "r")
lineas_a_leer = int(input("Ingrese las lineas que desea leer: "))

cantidad_de_lineas_a_leer = ArchiveLine(nombre_archivo, lineas_a_leer)
cantidad_de_lineas_a_leer.set_read(nombre_archivo)
cantidad_de_lineas_a_leer.get_read()