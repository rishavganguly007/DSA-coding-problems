# code -> https://leetcode.com/problems/surrounded-regions/
# resource -> https://www.youtube.com/watch?v=BtdgAys4yMk

'''
- check all the boundaries (left right up and down) for any "O"
- if "O" found run dfs/ bfs to find all the connected "O"s and mark them visted
- now traverse the matrix to find "O" whic were not visted, because those are the ones that ar not connected to boundaries
- replace them with "X"
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        vis = set()
        row = len(board)
        col = len(board[0])


        def dfs(i, j):
            vis.add((i, j))

            dir = [[0,1], [1, 0], [0, -1], [-1, 0]]

            for dr, dc in dir:
                r = i + dr
                c = j + dc

                if (r in range(row)) and (c in range(col)) and (board[r][c] == "O") and ((r,c) not in vis):
                    dfs(r, c)

        # traverse the 1st and last rows
        for j in range(col):
            if (board[0][j] == "O") and ((0,j) not in vis):
                dfs(0, j)

            if (board[row - 1][j] == "O") and ((row -1,j) not in vis):
                dfs(row -1, j)

        # traverse the left and right rows
        for i in range(row):
            if (board[i][0] == "O") and ((i, 0) not in vis):
                dfs(i, 0)
            
            if (board[i][col - 1] == "O") and ((i, col - 1) not in vis):
                dfs(i, col - 1) 
        
        for i in range(row):
            for j in range(col):
                if (board[i][j] == "O") and ((i,j) not in vis):
                    board[i][j] = "X"
        
        return board
