# code -> https://leetcode.com/problems/search-in-rotated-sorted-array
# resource -> https://www.youtube.com/watch?v=5qGrJbHhqFs

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right :
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            # to check if left part is sorted, i.e extreme left <= mid
            if nums[left] <= nums[mid] :
                # to check, nums[left] <= target <= nums[mid]
                if target >= nums[left] and target <= nums[mid]:
                    right = mid -1
                else: 
                    left = mid + 1
            # to check if right part is sorted, i.e extreme right > mid
            else:
                # to check, nums[mid] <= target <= nums[right] 
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1
