#code: https://leetcode.com/problems/partition-equal-subset-sum/description/?envType=problem-list-v2&envId=50vlu3z5&difficulty=MEDIUM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]
        
        # Initialize the dp array
        for ind in range(len(nums)):
            dp[ind][0] = True
        if nums[0] <= target:
            dp[0][nums[0]] = True

        # Populate the dp array
        for ind in range(1, len(nums)):
            for t in range(1, target + 1):
                # notTake = dp[ind - 1][t]
                # take = False
                # if nums[ind] <= t:
                #     take = dp[ind - 1][t - nums[ind]]
                # dp[ind][t] = take or notTake
                dp[ind][t] = dp[ind-1][t] or ((nums[ind] <= t) and dp[ind-1][t - nums[ind]])
        
        return dp[len(nums) - 1][target]
    

    def canPartition2(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        target = sum(nums) // 2
        dp = [[None for _ in range(10**4)] for _ in range( 10**4)]

        def f(ind, t):
            # print(ind, t)
            if dp[ind][t] != None:
                return dp[ind][t]
            if t == 0:
                dp[ind][t] = True
                return dp[ind][t]
            if ind == 0:
                dp[ind][t] = t == nums[ind]
                return dp[ind][t]

            notTake = f(ind-1, t)
            take = False
            if nums[ind] <= t:
                take = f(ind-1, t - nums[ind])
            dp[ind][t] = take or notTake
            return dp[ind][t]
        return f(len(nums)-1, target)
