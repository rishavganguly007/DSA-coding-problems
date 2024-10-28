# code -> https://leetcode.com/problems/counting-bits/description/?envType=problem-list-v2&envId=50vlu3z5&difficulty=EASY
class Solution:
    '''
    0 : 0000 
    1 : 0001 1 + dp[1 - 1]
    2 : 0010 1 + dp[2 - 2]
    3 : 0011 1 + dp[3 - 2]
    4 : 0100 1 + dp[4 - 4]
    5 : 0101 1 + dp[5 - 4]
    6 : 0110 1 + dp[6 - 4]
    7 : 0111 1 + dp[7 - 4]
    8 : 1000 1 + dp[8 - 8]
    '''
    def countBits(self, n: int) -> List[int]:

        dp = [0] * (n+ 1)
        offset = 1

        for i in range(1,n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp
        
