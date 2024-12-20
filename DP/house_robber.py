#code: https://leetcode.com/problems/house-robber/?envType=problem-list-v2&envId=50vlu3z5&difficulty=MEDIUM

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        dp[0] = nums[0]

        for i in range(1,len(nums)):
            if i-2>= 0:
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            else:
                dp[i] = max(dp[i-1], nums[i])
        return dp[len(nums)-1]
        
    def rob2(self, nums: List[int]) -> int:
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
        
        
