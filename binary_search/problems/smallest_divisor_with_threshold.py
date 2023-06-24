# code -> https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/

import math
class Solution:
    def checkThreshold(self,nums, threshold, mid):
        n = len(nums)
        sum = 0
        for i in range(n):
            sum += math.ceil(nums[i] / mid)
        return sum <= threshold


    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        high, low = max(nums), 1
        ans  = high
        '''
          take a eg, [1,2, 5, 9], threshold = 6
          if divisor is 9, arr[i] / 9 = 1, sum(arr) = 4 which is <= 6 
          if so any divisor > 5 < 9 will yeild same result
          so we have to take low = 1, high = max(arr) and have to check lower and lower
        '''
        while low <= high:
            mid = (low + high) // 2
            if self.checkThreshold(nums, threshold, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
