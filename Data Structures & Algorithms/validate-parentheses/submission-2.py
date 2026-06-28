class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {"]" : "[", ")" : "(", ">" : "<", "}" : "{"}

        stack = []
        for i in range(len(s)):
            if s[i] not in bracket:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                else:
                    if bracket[s[i]] != stack.pop():
                        return False
        if len(stack) != 0:
            return False
        return True