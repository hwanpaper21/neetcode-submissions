class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans =  ans + str(len(i)) + '#' + i
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            temp = s[j+1:j+1+int(s[i:j])]
            print(temp)
            i = j + 1 + int(s[i:j])
            ans.append(temp)
        return ans