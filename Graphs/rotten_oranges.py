# code -> https://leetcode.com/problems/rotting-oranges/
# resource -> https://www.youtube.com/watch?v=yf3oUhkvqA0&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=6

from Queue import Queue

class Pairs:
    def __init__(self, r, c, tm):
        self.r = r
        self.c = c
        self.tm = tm


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for i in range(m)] for j in range(n)]
        q = Queue()
        cntFresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.put(Pairs(i,j,0))
                    vis[i][j] = 2
                else:
                    vis[i][j] = 0
                if grid[i][j] == 1:
                    cntFresh += 1
        if cntFresh == 0:
            return 0
        tm = 0
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        cnt = 0
        while(not q.empty()):
            ele = q.get()
            r = ele.r
            c = ele.c
            t = ele.tm
            tm = max(tm, t)
            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]

                if( nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and vis[nrow][ncol] == 0 and grid[nrow][ncol] == 1):
                    vis[nrow][ncol] = 2
                    q.put(Pairs(nrow, ncol, t + 1))
                    cnt += 1

        if cnt != cntFresh:
            return -1
        return tm
        

