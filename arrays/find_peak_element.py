# code -> https://leetcode.com/problems/find-peak-element/description/

def findPeakElement(nums: List[int]) -> int:
        n = len(nums)
        # to check, if there is any single element, return the 1st index
        if n == 1:
            return 0
        left, right = 0, n

        while left <= right:
            
            mid = (left + right) // 2

            # to check if there is only 2 elements
            if mid == 0:
                return 0 if nums[0] >= nums[1] else 1
            # to check the last element, to avoid edge cases
            if mid == n - 1:
                return n - 1 if nums[n - 1] >= nums[n - 2] else n - 2   
            # peak is there if arr[x-1] < arr[x] > arr[x-1]
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1] :
                return mid
            # iif mid is larger, which peak must be on the right side, hence eliminate left
            if nums[mid - 1] < nums[mid]:
                left = mid + 1
            # else of the above case
            if nums[mid -1] > nums[mid]:
                right = mid - 1
        return -1

arr = [1,2,1,3,5,6,4]
print(findPeakElement(arr))
