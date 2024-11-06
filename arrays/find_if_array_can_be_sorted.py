# code: https://leetcode.com/problems/find-if-array-can-be-sorted/
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        prev_max = float('-inf')
        curr_max = nums[0]
        curr_min = nums[0]
        set_bits = self.count_bits(nums[0])

        for i in range(1, len(nums)):
            if set_bits == self.count_bits(nums[i]):
                curr_max = max(curr_max, nums[i])
                curr_min = min(curr_min, nums[i])
            else:
                if curr_min < prev_max:
                    return False

                prev_max = curr_max
                set_bits = self.count_bits(nums[i])
                curr_min = nums[i]
                curr_max = nums[i]

        return curr_min > prev_max

    def count_bits(self, num):
        return bin(num).count('1')
