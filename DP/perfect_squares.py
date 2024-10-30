# code: https://leetcode.com/problems/perfect-squares/?envType=problem-list-v2&envId=50vlu3z5&difficulty=MEDIUM
# same as code change
import math
class Solution:

    def numSquares(self, n: int) -> int:
        # tabulation
        dp = [0] + [float('inf')]*n
        max_squared = int(sqrt(n))

        for i in range(1, max_squared+1):
            squared = i*i
            for j in range(squared, n+1):
                dp[j] = min(dp[j], dp[j - squared]+1)
            print(i, " : ", dp)
        return dp[n]



    def numSquares2(self, n: int) -> int:
        MAX = 10**9
        k = int(math.isqrt(n))
        dp = [[MAX for _ in range(n+1)] for _ in range(k+1)] 
        def f(ind, t):
            if dp[ind][t] != MAX:
                return dp[ind][t]
            if t == 0:
                dp[ind][t] = 0
                return dp[ind][t]
            if ind == 1:
                dp[ind][t] = t
                return dp[ind][t]

            notTake = f(ind-1, t)
            take = MAX
            if ind**2 <= t:
                take = 1 + f(ind, t - ind**2)
            dp[ind][t] = min(take, notTake)
            return dp[ind][t]
        res = f(k, n)
        return res

        
