# code: 
# resource : logic same as last commit

from collections import defaultdict
class Solution:

    def getCount(self, nums, k):
        if k < 0:
            return 0
        l, r, count, distints = 0, 0, 0, 0
        mp = defaultdict(int)
        while r < len(nums):
            mp[nums[r]] +=1

            while len(mp) > k:
                mp[nums[l]] -= 1
                if mp[nums[l]] == 0:
                    mp.pop(nums[l])
                l += 1
            count += (r - l + 1)
            r+= 1
        return count

            
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.getCount(nums, k) - self.getCount(nums, k-1)
         
