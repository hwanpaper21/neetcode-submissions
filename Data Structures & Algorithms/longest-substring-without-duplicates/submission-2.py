class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slst = list(s)
        temp = []
        counter = 1
        max = 0
        for i in range(len(slst)):
            pointer = i + 1
            temp.append(slst[i])
            while pointer < len(slst):
                if slst[pointer] not in temp:
                    temp.append(slst[pointer])
                    counter += 1
                    pointer += 1
                    
                else:
                    pointer = len(slst)
            if max < counter:
                max = counter
            counter = 1
            temp = []
        return max
                