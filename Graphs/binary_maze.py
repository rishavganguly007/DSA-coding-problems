# code : https://leetcode.com/problems/shortest-path-in-binary-matrix/
# resource : https://www.youtube.com/watch?v=U5Mw4eyUmw4

from queue import Queue
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Check if the starting point is blocked
        if grid[0][0] == 1:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        
        # Initialize distance matrix with infinity
        dist = [[float('inf')] * cols for _ in range(rows)]
        
        # Use a queue for BFS traversal
        q = Queue()
        q.put((0, (0, 0)))  # Enqueue the source node with distance 0

        # Handle the edge case where source is the destination
        if rows == 1 and cols == 1:
            return 1 if grid[0][0] == 0 else -1

        # Define 8 possible directions (cardinal and diagonal)
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        
        # Perform BFS traversal / Djikstras Algo
        while not q.empty():
            dis, node = q.get()
            node_row, node_col = node

            # Explore neighbors in all 8 directions
            for dr, dc in dir:
                r = node_row + dr
                c = node_col + dc

                # Check if the neighbor is within the grid boundaries, is clear (0), and has a shorter path
                if (r in range(rows)) and (c in range(cols)) and (grid[r][c] == 0) and dis + 1 < dist[r][c]:
                    dist[r][c] = 1 + dis
                    q.put((dis + 1, (r, c)))  # Enqueue the updated distance and neighbor coordinates

        # Check if the destination cell is unreachable
        if dist[rows - 1][cols - 1] == float('inf'):
            return -1
        else:
            return dist[rows - 1][cols - 1] + 1 
