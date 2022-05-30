class AgregarDatos:

    def __init__(self, lectura):
        self.lectura = lectura
    
    def agregar_texto(self, modificacion):
        self.lectura.write(modificacion + "\n")
        return modificacion

    def set_read(self, read):
        self.lectura = read
        

    def get_read(self):
        for linea in self.lectura:
            print(linea)

ruta_lectura = open(r"C:\Users\devil\OneDrive\Escritorio\Universidad\COMPUTACION\TPN2 -PARTE 2\archivo_txt\ejercicio_n_3.txt", "r+")
agregar_lineas = (input("Ingrese el texto que desea guardar en un archivo txt: "))
agregar = AgregarDatos(ruta_lectura)  
agregar.set_read(ruta_lectura)
agregar.get_read()
print(agregar.agregar_texto(agregar_lineas))

