# code: https://leetcode.com/problems/minimum-array-end/
# res: https://leetcode.com/problems/minimum-array-end/solutions/6024884/beats-100-o-1-short-simple-explained-bitmasking
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x
        remaining = n - 1
        position = 1
    
        while remaining:
            if not (x & position):
                result |= (remaining & 1) * position
                remaining >>= 1
            position <<= 1
    
        return result
