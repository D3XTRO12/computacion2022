from itertools import islice
class ArchivoLinea:

    def __init__(self, archivo, cantidad_de_lineas):
        self.archivo = archivo
        self.cantidad_de_lineas = cantidad_de_lineas


    def set_read(self, read):
        self.archivo = read
    

    def get_read(self):
        for lineas in islice(self.archivo, self.cantidad_de_lineas):
            print(lineas)
        

ruta = open(r"C:\Users\devil\OneDrive\Escritorio\Universidad\COMPUTACION\TPN2 -PARTE 2\archivo_txt\ejercicio_n_2.txt", "r")
lineas_a_leer = int(input("Ingrese las lineas que desea leer: "))

cantidad_de_lineas_a_leer = ArchivoLinea(ruta, lineas_a_leer)
cantidad_de_lineas_a_leer.set_read(ruta)
cantidad_de_lineas_a_leer.get_read()