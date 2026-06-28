class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        temp = 0
        for i in range (len(prices)):
            count = i
            curr = prices[i]
            while count < len(prices):
                if temp < prices[count] - curr:
                    temp = prices[count] - curr
                count += 1
        return temp