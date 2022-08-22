class FileCopy:

    def __init__(self, read_file, write_file):
        self.read_file = read_file
        self.write_file = write_file


    def copy_file(self):
        for line in self.read_file:
            self.write_file.write(line)

with open(r"/home/d3xtro/Documents/computacion/TP2-P2/archivos txt/ej5.txt", "r") as read_file:
    with open(r"/home/d3xtro/Documents/computacion/TP2-P2/archivos txt/ej5-copy.txt", "w") as write_file:
        file_copy = FileCopy(read_file, write_file)
        file_copy.copy_file()