class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        ans = []
        counter = 0
        for i in nums:
            prod = 1
            nums.remove(i)
            for num in nums:
                prod = prod * num
            ans.append(prod)
            nums.insert(counter,i)
            counter += 1
        return ans