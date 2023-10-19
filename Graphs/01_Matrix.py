# code-> https://leetcode.com/problems/01-matrix/
# resource -> https://www.youtube.com/watch?v=edXdVwkYHF8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=13

from Queue import Queue
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(mat)
        m = len(mat[0])
        vis = [[ 0 for i in range(m)] for j in range(n)]
        dist = [[ 0 for i in range(m)] for j in range(n)]
        q = Queue()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    vis[i][j] = 1
                    q.put([i, j, 0])

        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        while not q.empty():
            ele = q.get()
            r = ele[0]
            c = ele[1]
            step = ele[2]
            dist[r][c] = step
            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]

                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and vis[nrow][ncol] == 0:
                    q.put([nrow, ncol, step +1])
                    vis[nrow][ncol] = 1
                    
        return dist


        
