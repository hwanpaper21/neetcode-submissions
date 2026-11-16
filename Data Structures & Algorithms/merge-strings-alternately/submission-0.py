class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        pt1 = 0
        pt2 = 0

        while len(word1) > pt1 or len(word2) > pt2:
            if len(word1) -1 < pt1:
                ans += word2[pt2]
                pt2 += 1
            elif len(word2)-1 < pt2:
                ans += word1[pt1]
                pt1 += 1
            else:
                ans = ans + word1[pt1] + word2[pt2]
                pt1 += 1
                pt2 += 1
        return ans
            