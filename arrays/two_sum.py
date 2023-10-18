#code -> https://leetcode.com/problems/two-sum/

class Solution(object):
    def if_Val_Is_Returned_Instead_Of_Index(self, nums, target):
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] + nums[right] > target: right -= 1
            elif nums[left] + nums[right] < target: left += 1
            else:
                return [nums[left], nums[right]]
        return[-1, -1]

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}

        for i in range(len(nums)):
            num = nums[i]
            extra = target - nums[i]
            if extra in dic:
                return [i, dic[extra]]
            dic[nums[i]] = i  
        return [-1, -1]

        
        
