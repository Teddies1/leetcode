class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            current_min = min(current_min, prices[i])
            max_profit = max(max_profit, prices[i] - current_min)
            
        return max_profit
            