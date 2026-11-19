class MyHashSet:

    def __init__(self):
        self.cur = []
        

    def add(self, key: int) -> None:
        if key not in self.cur:
            self.cur.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.cur:
            self.cur.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.cur:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)