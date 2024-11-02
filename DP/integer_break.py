#code: https://leetcode.com/problems/integer-break/?envType=problem-list-v2&envId=50vlu3z5&difficulty=MEDIUM

class Solution:
    # expl -> https://leetcode.com/problems/integer-break/solutions/285876/python-o-1-one-line-solution-detailed-explanation
    def integerBreak(self, n: int) -> int:
        case = [0,0,1,2,4,6,9]
        if n < 7:
            return case[n]
        dp = case + [0]*(n -6)
        for i in range(7, n+1):
            dp[i] = 3*dp[i-3]
        return dp[-1]
