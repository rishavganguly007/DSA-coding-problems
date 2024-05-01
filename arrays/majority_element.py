# code: https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        store = -1
        for i in range(len(nums)):
            if count == 0:
                store = nums[i]
                count += 1
            elif store == nums[i]:
                count += 1
            else:
                count -= 1
        return store
        
