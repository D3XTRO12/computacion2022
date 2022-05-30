class ArchivoLista:

    def __init__(self, arch):
        self.archivo = arch


    def leer_archivo(self):

        self.archivo = archivo.readlines()


    def ver_archivo_formato_lista(self):

        for lista in self.archivo:
            if lista[-1]=="\n":
                dato=lista[:-1].split(", ")
            else:
                dato=lista.split(", ")
            print(dato)


archivo = open(r"C:\Users\devil\OneDrive\Escritorio\Universidad\COMPUTACION\TPN2 -PARTE 2\archivo_txt\ejercicio_n_4.txt", "r")
archivo_list = ArchivoLista(archivo)
archivo_list.leer_archivo()
archivo_list.ver_archivo_formato_lista()