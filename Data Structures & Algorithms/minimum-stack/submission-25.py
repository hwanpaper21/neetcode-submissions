class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif self.min_stack[0] > val:
            self.min_stack.pop()
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        #print("pop1",self.stack)

    def top(self) -> int:
        #print("top", self.stack, len(self.stack)-1)
        #print("getmin", self.stack, self.stack[len(self.stack)-1])
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        temp = self.stack.copy()
        temp.sort()
        
        return temp[0]
