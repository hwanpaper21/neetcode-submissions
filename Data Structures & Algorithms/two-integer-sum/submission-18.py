class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos1 = 0
        

        for i in nums:
            pos2 = pos1 + 1
            for j in nums[pos2:len(nums)]:
                if i+j == target:
                    return [pos1, pos2]
                else:
                    pos2 += 1
            pos1 += 1
        return False