class Hashtable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for itm, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][itm] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        
        for item, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][item]

hash = Hashtable()
print(hash.get_hash("march 154"))
print(hash.get_hash("march 6"))
hash["march 6"] = 10
hash["march 154"] = 19
# print(hash["march 154"])
del hash["march 154"]
print(hash.arr)