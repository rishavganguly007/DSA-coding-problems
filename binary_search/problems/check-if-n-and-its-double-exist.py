# code: https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        arr.sort()
        for i, num in enumerate(arr):
            target = 2 * num
            lo, hi = 0, len(arr) - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if arr[mid] == target and mid != i:
                    return True
                if arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False
