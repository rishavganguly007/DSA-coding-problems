#code: https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/?envType=problem-list-v2&envId=50vlu3z5&difficulty=HARD
class Solution:
    def getBigger(self, notTake, take):
        if '0' in notTake:
            return take
        elif '0' in take:
            return notTake
        
        # Compare based on string length first.
        if len(take) > len(notTake):
            return take
        elif len(take) < len(notTake):
            return notTake
    
        # If lengths are equal, perform lexicographical comparison.
        return take if take > notTake else notTake

    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [['' for _ in range(target+1)] for _ in range(len(cost)+1)]
        def f(i, t):
            #base casse
            if t == 0:
                dp[i][t] = ''
                return dp[i][t]
            elif t < 0 or i >= len(cost)+1:
                return '0'
            if dp[i][t] != '':
                return dp[i][t]
            # dec1, dec2
            notTake = f(i+1, t)
            take = str(i) + f(1, t - cost[i-1])
            # max(dec1, dec2)
            dp[i][t] = self.getBigger(notTake, take)
            return dp[i][t]
        ans = f(1, target)
        return ans if '0' not in ans else '0'

        
