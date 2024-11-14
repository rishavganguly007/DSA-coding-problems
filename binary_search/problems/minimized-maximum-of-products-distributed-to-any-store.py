#code: https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/description/

class Solution:
    #code: https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/solutions/1563739/java-c-python-binary-search
    def minimizedMaximum(self, n, Q):
        beg, end = 0, max(Q)
        
        while beg + 1 < end:
            mid = (beg + end)//2
            if sum(ceil(i/mid) for i in Q) <= n:
                end = mid
            else:
                beg = mid
        
        return end
        
