class ContentTxt:

    def __init__(self, file_name, line_num, word_num, character_num):
        self.file_name = file_name
        self.line_num = line_num
        self.word_num = word_num
        self.character_num = character_num

    def read_file_content(self):
        for line in self.file_name:
            word = line.split()
            self.line_num += 1
            self.word_num += len(word)
            self.character_num += len(line)

    def print_content(self):
        print(f"El archivo contiene : {self.line_num} lineas")
        print(f"El archivo contiene : {self.word_num} palabras")
        print(f"El archivo contiene : {self.character_num} caracteres")

file_name = input("Ingresa el nombre del archivo:")

line_num = 0
word_num = 0
character_num = 0

with open(file_name, 'r') as archive:
    lectura = ContentTxt(archive, line_num, word_num, character_num)
    lectura.read_file_content()
    lectura.print_content()