class HashTable:
    def __init__(self) -> None:
        self.table = [None] * 127
    
    def hash_function(self, value):
        key=0
        for i in range (0, len(value)):
            key += ord(value[i])
        return key%127 
    
    def add(self, value):
        h = self.hash_function(value)
        if self.table[h] is None:
            self.arr[h] = value

    def search(self,value): 
        h = self.hash_function(value)
        if self.table[h] is None:
            return None
        else:
            return hex(id(self.table[h]))
  
    def remove(self,value): 
        h = self.hash_function(value)
        if self.table[h] is None:
            print("No hay elementos con ese valor", value)
        else:
            print("Elemento con valor", value, "eliminado")
            self.table[h] is None  

H = HashTable()
H.insert("A")
H.insert("B")
H.insert("C")

print(H.search("C"))