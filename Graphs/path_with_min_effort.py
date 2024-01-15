from queue import PriorityQueue
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pq = PriorityQueue()

        row = len(heights)
        col = len(heights[0])

        dist = [[float('inf')] * col] * row
        dist[0][0] = 0
        pq.put((0, (0,0)))

        dir = [[0,1],[0, -1], [1, 0], [-1, 0]]
        while not pq.empty():
            diff, node = pq.get()
            nr, nc = node

            if nr == row -1 and nc == col -1:
                return diff

            for r,c in dir:
                rw = nr + r
                cl = nc + c

                if (rw in range(row)) and (cl in range(col)):
                    newEffort = max(abs(heights[nr][nc] - heights[rw][cl]), diff)

                    if newEffort < dist[rw][cl]:
                        dist[rw][cl] = newEffort
                        pq.put((newEffort, (rw,cl)))
        return 0
