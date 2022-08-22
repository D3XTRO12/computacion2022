from datetime import date


class ArchiveList:

    def __init__(self, arch):
        self.archive = arch


    def read_archives(self):

        self.archive = archive.readlines()


    def see_format_list_archive(self):

        for list in self.archive:
            if list[-1]=="\n":
                date=list[:-1].split(", ")
            else:
                date=list.split(", ")
            print(date)


archive = open(r"/home/d3xtro/Documents/computacion/TP2-P2/archivos txt/ej4.txt", "r")
archive_list = ArchiveList(archive)
archive_list.read_archives()
archive_list.see_format_list_archive()