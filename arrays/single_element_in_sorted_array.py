# code -> https://leetcode.com/problems/single-element-in-a-sorted-array/description/
# resource -> https://www.youtube.com/watch?v=AZOmHuHadxQ

def singleNonDuplicate(nums: List[int]) -> int:
        '''
        suppose for the indexes,
        (even, odd) -> element is on right half, because we havent found the unique element
        (odd, even) -> element is on left have, we have passed through the unique element

        '''
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]
        
        left, right = 1, n-2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            '''
             if it's true, then i'm at left half, and ele is located at right half,
             so we have to eliminate the left half
            '''
            if ((mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1] )):
                left = mid + 1
            
            else:
                right = mid -1

        return -1
