class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numlst = set()

        for i in nums:
            if i not in numlst:
                numlst.add(i)
            elif i in numlst:
                return i
        
        print(numlst)