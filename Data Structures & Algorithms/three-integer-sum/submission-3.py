class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)-2):
            curr = i
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                tempSum = nums[curr] + nums[left] + nums[right]
                if  tempSum == 0:
                    temp = [nums[curr], nums[left], nums[right]]
                    if temp not in ans:
                        ans.append(temp)
                    left += 1
                elif tempSum > 0:
                    right -= 1
                else:
                    left += 1
        return(ans)
