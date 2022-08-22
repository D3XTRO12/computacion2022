from http import client
from secrets import choice
from typing import List
from class_book import *
from class_costumer import *
import pprint

class Library():
   
    __list_of_availible_books = []
    __client_list = []
    __book_dictionary = {}
    __client_dictionary = {} 


    def set_book_list(self, lista):
        self.__list_of_availible_books = lista


    def set_client_list(self, lista):
        self.__client_list = lista


    def add_client(self):
        name = input("Ingrese su nombre completo:")
        age = int(input("Ingrese su edad:"))
        adress = input("Ingrese su dirección de vivienda:")
        custumer = Custumer(name, age, adress)
        self.__client_list.append(custumer)


    def add_books(self):
        title = input("Ingresa el titulo del libro: ")
        author = input("Ingresa el nombre del autor: ")
        cost = int(input("Ingresa el monto total del libro: "))
        book = Book(title, author, cost)
        book.set_title(title)
        book.set_author(author)
        book.set_cost(cost)
        self.__list_of_availible_books.append(book)


    def show_books(self):
        contador = 0
        for x in self.__list_of_availible_books:
            contador = contador + 1
            print("\n", contador)
            print("\nEl nombre del libro es: ", x.get_title())
        input("Presiona enter para volver al menu.......")


    def view_book(self):
        contador = 0
        for x in self.__list_of_availible_books:
            contador = contador + 1
            print("\n", contador)
            print("\nEl nombre del libro es: ", x.get_title(), "\nEl autor del libro es:", x.get_author(), "\nEl precio del libro es: ", x.get_cost())
        input("Presiona enter para volver al menu.......")


    def show_clients(self):
        contador = 0
        for x in self.__client_list:
            contador = contador + 1
            print("\n", contador)
            print("\nEl nombre del cliente es:", x.get_name())
        input("Presiona enter para volver al menu.......")


    def view_custumers(self):
        contador = 0
        for x in self.__client_list:
            contador = contador + 1
            print("\n", contador)
            print("\nEl nombre del cliente es: ", x.get_name(), "\nLa edad del cliente es:", x.get_age(), "\nLa dirección de vivienda del cliente es: ", x.get_adress())
        input("Presiona enter para volver al menu.......")


    def assign(self):
        for i in self.__client_list:
                self.__client_dictionary = {"id": i.get_id(),
                                               "Nombre del cliente": i.get_name()}
                print(self.__client_dictionary)
        for x in self.__list_of_availible_books:
                self.__book_dictionary = {"id": x.get_id(),
                                             "Nombre del libro": x.get_title()}
                print(self.__book_dictionary)
        nombre_cliente = input("Ingresa el numero de cliente para asociarlo al libro que requiera: ")
        nombre_libro = input("Ingresa el numero del libro para asociarlo con el cliente: ")
        if nombre_cliente == self.__client_dictionary['Nombre del cliente'] and nombre_libro == self.__book_dictionary['Nombre del libro']:
            self.__client_dictionary.update(self.__book_dictionary)
            input("Presiona enter para volver al menu.......")
    
    
    def show_assing(self):
        print(self.__client_dictionary)
        input("Presiona enter para volver al menu.......")