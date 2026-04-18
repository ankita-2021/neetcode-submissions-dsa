class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            sell = prices[i]
            for j in range(i+1, len(prices)):
                if prices[j] > sell:
                    sell = prices[j]
            profit = sell - prices[i]
            max_profit = max(max_profit, profit)
        return max_profit
