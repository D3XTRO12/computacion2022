class LecturaArchivo:
    def __init__(self, archivo) -> None:
        self.lectura = archivo

    def set_read(self, read):
        self.lectura = read
        

    def get_read(self):
        for linea in self.lectura:
            print(linea)

with open(r"C:\Users\devil\OneDrive\Escritorio\Universidad\COMPUTACION\TPN2 -PARTE 2\archivo_txt\ejercicio_n_1.txt","r") as archivo:
    lectura = LecturaArchivo(archivo)
    lectura.set_read(archivo)
    lectura.get_read()
    
