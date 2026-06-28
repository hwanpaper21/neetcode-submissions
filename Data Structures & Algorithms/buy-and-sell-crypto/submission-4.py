class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0   # 사는 날
        right = 1  # 파는 날

        max_profit = 0

        while right < len(prices):

            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right

            right += 1

        return max_profit