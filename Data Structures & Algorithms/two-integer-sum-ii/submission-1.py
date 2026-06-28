class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for one in range (len(numbers)):
            x = numbers[one]
            two = one + 1
            for two in range (len(numbers)):
                if x + numbers[two] == target:
                    return[one+1,two+1]
                else:
                    two += 1
            one += 1

        