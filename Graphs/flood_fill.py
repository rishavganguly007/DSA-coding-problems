# code -> https://leetcode.com/problems/flood-fill/

from queue import Queue

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        vis = set()

        rows = len(image)
        cols = len(image[0])
        
        def dfs(i,j):
            vis.add((i,j))
            temp_color = image[i][j]
            image[i][j] = color

            dir = [[0,1], [1, 0], [0, -1], [-1, 0]]
            for dr, dc in dir:
                    r = i + dr
                    c = j + dc

                    if (r in range(rows)) and (c in range(cols)) and (image[r][c] == temp_color) and ((r,c) not in vis):
                        # vis.add((r,c))
                        # image[r][c] = color
                        dfs(r,c)



        def bfs(i, j):
            q = Queue()
            vis.add((i, j))
            q.put((i,j))
            temp_color = image[i][j]
            image[i][j] = color

            while not q.empty():
                rw, cl = q.get()
                dir = [[0,1], [1, 0], [0, -1], [-1, 0]]

                for dr, dc in dir:
                    r = rw + dr
                    c = cl + dc

                    if (r in range(rows)) and (c in range(cols)) and (image[r][c] == temp_color) and ((r,c) not in vis):
                        q.put((r,c))
                        vis.add((r,c))
                        image[r][c] = color


       # bfs(sr, sc)
        dfs(sr, sc) 
        
        return image

        
