class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        count = 0
        while count < len(word1) and count < len(word2):
            ans += word1[count]
            ans += word2[count]
            count += 1
        ans += word1[count:]
        ans += word2[count:]
        return ans