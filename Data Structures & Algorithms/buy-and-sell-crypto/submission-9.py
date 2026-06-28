class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in prices:
            if min_price > i:
                min_price = i
            elif max_profit < i - min_price:
                print (i,min_price)
                max_profit = i - min_price
        return max_profit