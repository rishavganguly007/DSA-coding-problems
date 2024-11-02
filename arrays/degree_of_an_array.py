# code: https://leetcode.com/problems/degree-of-an-array/
from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        print(d.values())
        maxi = -1
        min_size = float('inf')
        for i in d.values():
            count = len(i)
            if count > maxi:
                size = i[-1] - i[0] + 1
                min_size = size
                maxi = count
            elif count == maxi:
                size = i[-1] - i[0] + 1
                min_size = min(min_size, size)
        return min_size
