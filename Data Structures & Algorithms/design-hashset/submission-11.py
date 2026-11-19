class MyHashSet:

    def __init__(self):
        self.cur = [None] * (1*10**6+1)
        

    def add(self, key: int) -> None:
        self.cur[key] = key
        

    def remove(self, key: int) -> None:
        self.cur[key] = None

    def contains(self, key: int) -> bool:
        print(key, self.cur[key])
        if self.cur[key] != None:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)