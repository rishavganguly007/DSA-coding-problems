# code: https://leetcode.com/problems/binary-subarrays-with-sum/description/
# resource : https://youtu.be/XnMdNUkX6VM

class Solution:
    def getCount(self, nums, goal):
        '''
        returns the count of sub-array <= goal
        '''
        if goal < 0:
            return 0
        l, r, count, sum = 0 , 0, 0, 0

        while( r < len(nums)):
            sum += nums[r]
            while sum > goal:
                sum -= nums[l]
                l += 1
            count += (r - l + 1)
            r += 1
        
        return count
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        return self.getCount(nums, goal) - self.getCount(nums, goal-1)
