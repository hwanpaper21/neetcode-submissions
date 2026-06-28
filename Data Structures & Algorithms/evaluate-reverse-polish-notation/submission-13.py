class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        curr = 0
        next = 0
        lst = ['+', '-', '*', '/']
        
        if len(tokens) == 1:
            return int(tokens[0])
        for i in tokens:
            if i in lst:
                curr = int(stack.pop())
                next = int(stack.pop())
                if i == '+':
                    curr = next + curr
                elif i == '-':
                    curr = next - curr
                elif i == '*':
                    curr = next * curr
                elif i == '/':
                    curr = int(next / curr)
                stack.append(curr)
            else:
                stack.append(i)

        return curr
