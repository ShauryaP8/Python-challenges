class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def _hash_function(self,key):
        return key % self.size
    
    def insert(self, key, value):
        index = self._hash_function(key)
        for item in self.hash_table[index]:
            if item[0] == key:
                item[1] = value
                return
            
        self.hash_table[index].append([key, value])

    def find(self, key):
        index = self._hash_function(key)
        for item in self.hash_table[index]:
            if item[0] == key:
                return item[1]
            
        return None
    
    def delete(self,key):
        index = self._hash_function(key)
        for i, item in enumerate(self.hash_table[index]):
            if item[0] == key:
                del self.hash_table[index][i]
                return
            
        raise KeyError(f"Key '{key}' does not exist in the table")
    

#Example usage
hash_table = HashTable(10)

#insert items
hash_table.insert(3, 'apple')
hash_table.insert(13, 'banana')
hash_table.insert(23, 'orange')

#Find items
print(hash_table.find(13))
print(hash_table.find(20))

#Del items
hash_table.delete(3)
print(hash_table.find(3))
