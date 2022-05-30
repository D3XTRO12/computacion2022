from asyncore import read


class MapDelimiter:

    def __init__(self, file_name, separador) -> None:
        self.file_name = file_name
        self.separador = separador

    def add_delimitator(self):
        read = ' '.join(self.file_name)
        list = read.split(" ")
        read_new = self.separador.join(list)
        print(read_new)

file_name = input("Ingrese el archivo:")
separador = input("Ingrese el separador que desea utilizar: ")
with open(file_name, 'r') as archive:
    delimiter = MapDelimiter(archive, separador)
    delimiter.add_delimitator()