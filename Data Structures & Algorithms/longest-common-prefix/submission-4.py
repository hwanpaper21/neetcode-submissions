class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in strs:
                if len(j) <= i or j[i] != char:
                    return strs[0][:i]
        return strs[0]