# code -> https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def ifPossible(self,arr, day, m,k):
        seq = 0
        total = 0
        for i in range(len(arr)):
            if arr[i] <= day:
                seq +=1
            else:
                total += seq / k
                seq = 0
        total += seq / k
        return total >= m 

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        high = max(bloomDay)
        low = min(bloomDay)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if self.ifPossible(bloomDay, mid, m, k):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
