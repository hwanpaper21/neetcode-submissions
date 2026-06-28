class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums)-1
        left = 0

        while right >= left:
            mid = (right + left)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right -= 1
            elif target > nums[mid]:
                left += 1
        return -1
