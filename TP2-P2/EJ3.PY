from ast import Add


class AddDates:

    def __init__(self, lecture):
        self.lecture = lecture
    
    def add_text(self, changes):
        self.lecture.write(changes + "\n")
        return changes

    def set_read(self, read):
        self.lecture = read
        

    def get_read(self):
        for line in self.lecture:
            print(line)

lecture_rute = open(r"/home/d3xtro/Documents/computacion/TP2-P2/archivos txt/ej3.txt", "r+")
add_lines = (input("Ingrese el texto que desea guardar en un archivo txt: "))
add = AddDates(lecture_rute)  
add.set_read(lecture_rute)
add.get_read()
print(add.add_text(add_lines))
