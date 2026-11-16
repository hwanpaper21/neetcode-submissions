class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        ans = ""
        while len(strs[0]) > count:
            prefix = strs[0][0:count+1]
            for i in strs:
                if i[0:count+1] != prefix:
                    return ans
            
            ans = prefix
            count += 1
        return ans