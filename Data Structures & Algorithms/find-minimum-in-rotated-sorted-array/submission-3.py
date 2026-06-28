class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1

        while nums[left] > nums[right]:
            temp = nums.pop(right)
            nums.insert(0, temp)
        return nums[0]