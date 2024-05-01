# code: https://leetcode.com/problems/merge-sorted-array/description/
# soln: watch neetcode
"""
  Initial state:
        nums1: [1, 2, 3, _, _, _] (m = 3)
        nums2: [2, 5, 6]           (n = 3)

        Merge Process:
        ----------------
        nums1: [1, 2, 3, _, _, _] 
        nums2: [2, 5, 6]

        Comparing nums1[2] (3) with nums2[2] (6):
        3 > 6, so nums1[last] = nums1[5] = 3
        nums1: [1, 2, 3, _, _, 6]
        nums2: [2, 5, 6]

        Decreasing n by 1: n = 1
        Decreasing last by 1: last = 4
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1
        
