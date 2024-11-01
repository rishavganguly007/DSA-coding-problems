# code: https://leetcode.com/problems/knight-dialer/?envType=problem-list-v2&envId=50vlu3z5&difficulty=MEDIUM
class Solution:
    def knightDialer(self, n: int) -> int:
        if n== 1:
            return 10
        mod = 10**9+7
        jumps = [
            [4,6],
            [6,8],
            [7,9],
            [4,8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]
        dp = [1]*10

        for _ in range(n - 1):
            next = [0]*10
            for i in range(10):
                for j in jumps[i]:
                    next[j] = next[j] + dp[i]
            dp = next
        return sum(dp) % mod
        
