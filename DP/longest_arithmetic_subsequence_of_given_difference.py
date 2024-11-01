#code: https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/?envType=problem-list-v2&envId=50vlu3z5&difficulty=MEDIUM

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {}  # Stores the maximum length at each index
        
        ans = 1  # Initialize with the minimum length of 1
        
        for i in range(n):
            num = arr[i]
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1
            else:
                dp[num] = 1
            
            ans = max(ans, dp[num])
        
        return ans
    def longestSubsequence2(self, arr: List[int], difference: int) -> int:

        def f(i, prev):
            n = len(arr)
            if i >= n:
                return 0
            take, notTake = 0,0
            
            # if arr[i] + difference != arr[i+1]:
            #     return 0
            if prev == -10000:
                notTake = f(i+1, prev)
                take = 1+f(i+1, arr[i])
            else:
                notTake = f(i+1,prev)
                if arr[i] - prev == difference:
                    take = 1+f(i+1, arr[i])
            count = max(take, notTake)
            return count
        res = f(0, -10000)
        return res
        
