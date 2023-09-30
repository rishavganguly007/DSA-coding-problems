# code -> https://leetcode.com/problems/product-of-array-except-self/description/
# resource -> https://www.youtube.com/watch?v=bNvIQI2wAjk

"""
input -> [1,2,3,4]

- create a prefix array, prefix = [1,1,2,6]
- create a postfix array, postfix = [24,12,4,1]
- output res = [postfix[i] * prefix[i]]=[24,12,8,6]
"""
def productExceptSelf(nums):
    prefix = [1] * (len(nums))
    postfix = [1] * (len(nums))

    for i in range(1,len(nums)):
        prefix[i] = nums[i-1] * prefix[i - 1]

    for i in range(len(nums)-2, -1, -1):
        postfix[i] = nums[i+1] * postfix[i+1]
    
    res = [prefix[i]*postfix[i] for i in range(len(nums))]
    return res
  
def productExceptSelf_Optimised(nums):
  # optimised by not using the arrays but variable instead
        res = [1] * (len(nums))
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= res[i]
        for i in range(len(nums) - 1, -1 , -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

print(productExceptSelf_Optimised([1,2,3,4]))

