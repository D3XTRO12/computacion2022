class Book():

    def __init__(self, title, author, cost) -> None:
        self.__id = id
        self.__title = title
        self.__author = author
        self.__cost = cost

    
    def set_id(self, id):
        self.__id = id
        

    def set_title(self, title):
        self.__title = title


    def set_author(self, author):
        self.__author = author


    def set_cost(self, cost):
        self.__cost = cost


    def get_id(self):
        return self.__id


    def get_title(self):
        return self.__title


    def get_author(self):
        return self.__author

   
    def get_cost(self):
        return self.__cost