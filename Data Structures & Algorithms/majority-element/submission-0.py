class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countDict = {}
        max = 0
        major = 0
        for i in nums:
            if i in countDict:
                countDict[i] += 1
            else:
                countDict[i] = 1
        print(countDict)

        for j in countDict:
            if countDict[j] > max:
                major = j
                max = countDict[j]
        return major
        