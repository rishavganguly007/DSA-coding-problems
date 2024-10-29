# code -> https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]

        

        def f(ind, val):
            if dp[ind][val] != -1:
                return dp[ind][val]
            if ind == 0:
                if(val % coins[0] == 0):
                    dp[ind][val] = int(val / coins[0])
                    return dp[ind][val]
                else: 
                    dp[ind][val] = 10**9
                    return dp[ind][val]

            notTake = f(ind - 1, val)
            take = 10**9
            if coins[ind] <= val:
                take = 1 + f(ind, val - coins[ind])
            
            dp[ind][val] =  min(take, notTake)

            return dp[ind][val]

        res = f(len(coins) - 1, amount)

        return res if res != 10**9 else -1
        
