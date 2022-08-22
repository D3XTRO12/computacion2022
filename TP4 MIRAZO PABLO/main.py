from dbm.ndbm import library
from class_book import *
from class_costumer import *
from class_library import *



def menuinicio():
    while True:
            print("Bienvenidos a la bibloteca virtual, que desea realizar")
            print("1 = Agregar clientes:")
            print("2 = Agregar libros:")
            print("3 = Mostrar libros de la biblioteca:")
            print("4 = Mostrar clientes de la biblioteca:")
            print("5 = Ver información de cada libro:")
            print("6 = Ver información de cada cliente:")
            print("7 = Asignar un libro a un cliente:")
            print("8 = Ver libro asignado")
            print("9 = EXIT")
            choice = input("PRESIONE LAS SIGUIENTES OPCIONES PARA PODER EMPEZAR[1/2/3/4/5/6/7/8/9]  = ")
            if choice == '1':
                library.add_client()

            elif choice == '2':
                library.add_books()

            elif choice == '3':
                library.show_books()

            elif choice == "4":
                library.show_clients()

            elif choice == "5":
                library.view_book()

            elif choice == "6":
                library.view_custumers()

            elif choice == "7":
                library.assign()

            elif choice == "8":
                   
                library.show_assing()
            elif choice == '9':
                print(
                    "GRACIAS POR UTILIZAR NUESTRO SERVICIO.... ESPERAMOS QUE SE HAYA PODIDO INFORMAR... HASTA LA PRÓXIMA!!")
                break
            else:
                print("\n OPCION INCORRECTA.... VUELVA A ELEGIR UNA OPCION EXISTENTE EN EL SISTEMA....")

library = Library()

menuinicio()