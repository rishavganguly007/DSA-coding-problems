# code -> https://practice.geeksforgeeks.org/problems/aggressive-cows/1

from typing import List
class Solution:
    def isPossible(self,a: List[int], n: int, cows: int, minDist: int) -> bool:
        cntCows = 1
        lastPlacedCow = a[0]
        for i in range(1, n):
            if a[i] - lastPlacedCow >= minDist:
                cntCows += 1
                lastPlacedCow = a[i]


        if cntCows >= cows:
            return True
        return False



    def solve(self,n,k,stalls):
        stalls.sort()
        low = 1
        high = stalls[n - 1] - stalls[0]


        while low <= high:
            mid = (low + high) >> 1


            if self.isPossible(stalls, n, k, mid):
                low = mid + 1
            else:
                high = mid - 1


        return 
