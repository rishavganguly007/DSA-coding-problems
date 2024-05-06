# code: https://leetcode.com/problems/fruit-into-baskets/description/
# resource: https://www.youtube.com/watch?v=yYtaV0G3mWQ

"""
basically need to figure out a max subarray with only 2 unique nums

use a sliding window that goes till the end and stores fruittype, count in a map
and once key count goes > 2  decreament total, fruit-count and increment left pointer

return the maxTotal
"""

from collections import defaultdict 
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count  = defaultdict(int) # to store: fruitType -> count

        l, total, maxTotal = 0, 0, 0

        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1

            while len(count) > 2:
                f = fruits[l]

                count[f] -= 1
                total -= 1
                l += 1
                if not count[f]:
                    count.pop(f)
            maxTotal = max(total, maxTotal)

        return maxTotal

        
