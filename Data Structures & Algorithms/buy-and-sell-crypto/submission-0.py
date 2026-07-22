class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = sell - buy
        # profit = i - buy
        maxProfit = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right = right + 1
        return maxProfit
        