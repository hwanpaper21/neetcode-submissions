class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x = int(len(nums)/2)
        right = len(nums)-1
        left = 0
        if nums[x] > target:
            right = x
        elif nums[x] == target:
            return x
        else:
            left = x

        while right >= left:
            if target == nums[right]:
                return right
            right -= 1
        return -1
