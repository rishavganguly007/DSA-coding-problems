# code : https://leetcode.com/problems/count-number-of-nice-subarrays/description/
# resource : same prblm as Binary Subarrays With Sum

class Solution:
    def getCount(self, nums, k):
        if k < 0: 
            return 0
        l, r, count, oddCount = 0, 0, 0, 0
        
        while r < len(nums):
            if nums[r] % 2 !=  0:
                oddCount += 1
            while oddCount > k :
                if nums[l] % 2 != 0:
                    oddCount -= 1
                l+=1
            count += ( r - l + 1)
            r += 1
        return count

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.getCount(nums, k) - self.getCount(nums, k-1) 
