# code -> https://leetcode.com/problems/maximum-product-subarray/description/
# resource -> https://www.youtube.com/watch?v=hnswaLJvr6g

"""
use the postfix prefix appraoch to get the max product
"""
def maxProduct(self, nums: List[int]) -> int:
        maxi = (10 ** 6) *(-1)
        prefix = 1
        for i in range(len(nums)):
            prefix *= nums[i]
            maxi = max(maxi, prefix)
            if prefix == 0:
                prefix = 1
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            postfix *= nums[i]
            maxi = max(maxi, postfix) 
            if postfix == 0:
                postfix = 1       
        return maxi
