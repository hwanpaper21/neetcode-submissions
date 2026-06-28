class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        print("pop-1",self.stack)
        print("pop", len(self.stack)-1, self.stack[len(self.stack)-1])
        del self.stack[len(self.stack)-1]
        #print("pop1",self.stack)

    def top(self) -> int:
        #print("top", self.stack, len(self.stack)-1)
        #print("getmin", self.stack, self.stack[len(self.stack)-1])
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        temp = self.stack.copy()
        temp.sort()
        
        return temp[0]
