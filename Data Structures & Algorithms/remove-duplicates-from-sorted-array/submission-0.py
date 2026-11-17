class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        ans = []
        while right < len(nums):
            if nums[left] == nums[right]:
                nums.remove(nums[right])
            else:
                ans.append(left)
                left = right
                right += 1
        return len(nums)