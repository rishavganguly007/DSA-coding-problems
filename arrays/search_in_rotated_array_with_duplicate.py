# code -> https://leetcode.com/problems/search-in-rotated-sorted-array-ii
# resource -> https://www.youtube.com/watch?v=w2G2W8l__pc
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2
            if target ==  nums[mid]:
                return True
            # reducing the duplicates 1st, THE MAIN THING
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
            # Rest is same as without duplicates
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left =  mid + 1
                else:
                    right = mid -1 
        return False
