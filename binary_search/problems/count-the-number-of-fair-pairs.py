# code: https://leetcode.com/problems/count-the-number-of-fair-pairs/submissions/1451850456/
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def countLess(val: int) -> int:
            res, j = 0, len(nums) - 1
            for i in range(len(nums)):
                while i < j and nums[i] + nums[j] > val:
                    j -= 1
                res += max(0, j - i)
            return res
        nums.sort()
        return countLess(upper) - countLess(lower - 1)
