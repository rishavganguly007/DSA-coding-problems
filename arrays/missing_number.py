# code -> https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        act_sum = int(( n * (n + 1)) / 2)

        return abs(act_sum - s)
