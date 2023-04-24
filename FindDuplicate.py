def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if d.get(nums[i]) is not None:
                return nums[i]
            else:
                d[nums[i]] = 1
        return None
print(findDuplicate([1,1,1,3]))
