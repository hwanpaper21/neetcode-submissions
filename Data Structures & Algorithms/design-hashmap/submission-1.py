class MyHashMap:

    def __init__(self):
        self.hashkeys = [None] * (10**6 + 1)
        

    def put(self, key: int, value: int) -> None:
        self.hashkeys[key] = [key,value]

    def get(self, key: int) -> int:
        if self.hashkeys[key] != None:
            return self.hashkeys[key][1]
        else:
            return -1

    def remove(self, key: int) -> None:
        self.hashkeys[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)