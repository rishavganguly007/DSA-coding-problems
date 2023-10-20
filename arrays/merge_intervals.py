# code -> https://leetcode.com/problems/merge-intervals/
# resource -> https://www.youtube.com/watch?v=44H3cEC2fFM

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            last = res[-1][1]

            if last >= start:
                res[-1][1] = max(last, end)
            # [[1,3], [2,5]], 5 will be stored
            else:
                res.append([start, end])
        return res

        
