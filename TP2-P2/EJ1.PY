class ReadArchive:
    def __init__(self, read_file):
        self.lectura = read_file
    
    def set_read (self, read):    
        self.lectura = read
        for linea in lectura.get_read():
            print(linea)

    def get_read (self):
        return self.lectura

with open(r"/home/d3xtro/Documents/computacion/TP2-P2/archivos txt/ej1.txt", 'r') as archive:
    lectura = ReadArchive(archive)
    lectura.set_read(archive)
