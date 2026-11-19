class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pt = 0

        while pt < len(nums):
            print(nums[pt], nums)
            if nums[pt] == val:
                del nums[pt]
            else:
                pt += 1
        return len(nums)