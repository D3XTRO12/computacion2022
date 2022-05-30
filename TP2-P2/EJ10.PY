class LineExpresion:

    def __init__(self, file_name, sentence):
        self.file_name = file_name
        self.sentence = sentence

    
    def denotation_search(self):
        for i, line in enumerate(self.file_name.readlines(), 1):
            if self.sentence in line:
                print(f"La palabra ingresada: {self.sentence}\nEsta denotada en la linea: {i}\n")

filename = input("Ingrese el nombre del archivo a denotar: ")
sentence = input("Denote la oracion que desea buscar: ")
with open(filename, 'r') as archive:
    denotacion = LineExpresion(archive, sentence)
    denotacion.denotation_search()
