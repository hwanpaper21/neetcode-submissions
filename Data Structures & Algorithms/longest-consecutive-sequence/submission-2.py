class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        counter = 1
        maxseq = 1
        if len(nums) == 0:
            return 0
        for i in range (len(nums)-1):
            j = i+1
            if nums[i] +1 == nums[j]:
                counter += 1
                if maxseq < counter:
                    maxseq = counter
            elif nums[i] == nums[j]:
                continue
            else:
                if maxseq < counter:
                    maxseq = counter
                    print(maxseq, counter)
                counter = 1
        return maxseq

