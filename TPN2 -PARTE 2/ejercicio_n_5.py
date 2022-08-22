class ArchivoCopy:

    def __init__(self, leer_archivo, escribir_archivo) -> None:
        self.leer_archivo = leer_archivo
        self.escribir_archivo = escribir_archivo


    def copy_file(self):
        for line in self.leer_archivo:
            self.escribir_archivo.write(line)

with open(r"C:\Users\devil\OneDrive\Escritorio\Universidad\COMPUTACION\TPN2 -PARTE 2\archivo_txt\ejercicio_n_5.txt", "r") as read_file:
    with open(r"C:\Users\devil\OneDrive\Escritorio\Universidad\COMPUTACION\TPN2 -PARTE 2\archivo_txt\ejercicio_n_5_copy.txt", "w") as write_file:
        archivo_copia = ArchivoCopy(read_file, write_file)
        archivo_copia.copy_file()