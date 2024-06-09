# code: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/submissions/1282651712/
'''
sort the array do a sliding window
'''
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0
        nums.sort()
        l, r = 0, k - 1
        mini = float('inf')
        while( r < len(nums)):
            temp = nums[r] - nums[l]
            mini = min(mini, temp)
            l += 1
            r += 1
        return mini

        
