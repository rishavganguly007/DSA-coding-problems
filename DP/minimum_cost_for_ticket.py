#code -> https://leetcode.com/problems/minimum-cost-for-tickets/description/?envType=problem-list-v2&envId=50vlu3z5&difficulty=MEDIUM

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*367
        def sub(ind):
            n = len(days)
            if ind >= n:
                return 0
            if dp[ind] != 0:
                return dp[ind]

            cost_day = costs[0] + sub(ind + 1)

            i = ind
            while( i < n and days[i] < days[ind] + 7):
                i += 1
            cost_week = costs[1] + sub( i)

            i = ind
            while( i < n and days[i] < days[ind] + 30):
                i += 1
            cost_mons = costs[2] + sub(i)
 
            dp[ind] = min(cost_day, cost_week, cost_mons)
            return dp[ind]
        
        
        return sub(0)
        
