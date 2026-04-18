class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit  = 0
        idx = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                idx = i
                break
        sell = prices[idx]
        for j in range(idx, len(prices)):
            if prices[j] > sell:
                sell = prices[j]
        profit = sell - buy
        return profit
