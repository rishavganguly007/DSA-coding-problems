# code-> https://leetcode.com/problems/decode-ways/?envType=problem-list-v2&envId=50vlu3z5&difficulty=MEDIUM

class Solution:
    #res -> https://leetcode.com/problems/decode-ways/solutions/30451/evolve-from-recursion-to-dp
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        dp[n] = 1
        for i in range(n-1, -1,-1 ):

            if s[i] != '0':
                dp[i] = dp[i+1]
                if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                    dp[i] += dp[i+2]
        return dp[0]
    
    
    def numDecodings2(self, s: str) -> int:
        dp = [None]*len(s)
        def f(i):
            n = len(s)
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            if dp[i] is not None:
                return dp[i]
            
            # for single character decoding
            res = f(i + 1)
            
            # for two-character decoding
            if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                res += f(i + 2)
            
            dp[i] = res
            return dp[i] 
        return 0 if len(s)==0 else f(0)
