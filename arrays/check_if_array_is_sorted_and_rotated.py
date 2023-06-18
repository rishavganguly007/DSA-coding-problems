# code -> https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
def check(self, nums: List[int]) -> bool:
        n = len(nums)
        drop = 0
        for i in range(n -  1):
            if nums[i+1] >= nums[i]:
                continue
            else:
                drop += 1
        if nums[0] < nums[n-1] and drop > 0:
            return False 
        return True if drop == 0 or drop == 1 else False
arr = [3,4,5,1,2]
print(check(arr))
