# code -> https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# resource -> https://www.youtube.com/watch?v=nhEMDKMB44g&t=784s

def findMin(nums) -> int:
        left, right = 0, len(nums) - 1
        mid = 0
        ans = 10 ** 9
        while left <= right:
            mid = (left + right) // 2
            # left is sorted, then pick the min element and eliminate that half
            if nums[left] <= nums[mid]:
                ans = min(ans, nums[left])
                left = mid + 1
            else: 
                ans = min(ans, nums[mid])
                right =  mid - 1
        return ans
def findMax(nums) -> int:
        left, right = 0, len(nums) - 1
        mid = 0
        ans = (10 ** 9) * (-1)
        while left <= right:
            mid = (left + right) // 2
            # left is sorted, then pick the max element and eliminate that half
            if nums[left] <= nums[mid]:
                ans = max(ans, nums[mid])
                left = mid + 1
            else: 
                ans = max(ans, nums[right])
                right =  mid - 1
        return ans
arr = [4,5,6,7,0,1,2]
print(f"max: {findMax(arr)}, min: {findMin(arr)}")
