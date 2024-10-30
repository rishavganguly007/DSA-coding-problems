#code: https://leetcode.com/problems/house-robber/?envType=problem-list-v2&envId=50vlu3z5&difficulty=MEDIUM

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [-1] * len(nums)
        def f(ind):
            if dp[ind] != -1:
                return dp[ind]
            if ind < 0:
                dp[ind] = 0
                return dp[ind]
            if ind == 0:
                dp[ind] = nums[ind]
                return dp[ind]

            notTake = f(ind - 1)
            take = -1
            take = nums[ind] + f(ind-2)
            dp[ind] = max(notTake, take)
            return dp[ind]
        return f(len(nums)-1)
        
        
