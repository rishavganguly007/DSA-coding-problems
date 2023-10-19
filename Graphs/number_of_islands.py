# code -> https://leetcode.com/problems/number-of-islands/
# resource -> https://www.youtube.com/watch?v=pV2kpPD66nE
from Queue import Queue
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = Queue()
            visit.add((r,c))
            q.put((r,c))

            while not q.empty():
                rw, cl = q.get()
                dir = [[1,0], [0,1], [-1,0], [0,-1]]
                for dr, dc in dir:
                    _r, _c = rw + dr, cl + dc

                    if (_r in range(row)) and (_c in range(col)) and (grid[_r][_c] == "1") and ((_r, _c) not in visit):

                        q.put((_r, _c))
                        visit.add((_r, _c))
        for i in range(row):
            for j in range(col):
                if (grid[i][j] == "1") and ((i,j) not in visit):
                    bfs(i, j)
                    islands += 1
        return islands
        
