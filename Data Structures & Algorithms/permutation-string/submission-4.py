class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2) - len(s1)+1):
            temp = s2[i:len(s1)+i]
            #print(tuple(sorted(temp)))
            if tuple(sorted(s1)) == tuple(sorted(temp)):
                return True
        return False
        