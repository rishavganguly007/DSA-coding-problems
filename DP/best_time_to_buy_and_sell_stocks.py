# code -> https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# resource -> https://www.youtube.com/watch?v=excAOvwF_Wk

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxProfit = 0

        for i in range(len(prices)):
            cost = prices[i] - mini
            maxProfit = max(maxProfit, cost)
            mini = min(mini, prices[i])

        return maxProfit
        
