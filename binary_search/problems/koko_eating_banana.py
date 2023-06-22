# code -> https://leetcode.com/problems/koko-eating-bananas/description/
# resource -> https://www.youtube.com/watch?v=qyfekrNni90

import math
class Solution:
    def foo(self, piles, val):
        total = 0
        for i in range(len(piles)):
            total += math.ceil( piles[i]/ val)
        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles) // this the min num of hours that will validate h, above high all will validate h

        while(low <= high):
            mid = (low + high) // 2
            total = self.foo(piles, mid)
            if total <= h:
                high = mid -1
            else: 
                low = mid + 1
        return low
