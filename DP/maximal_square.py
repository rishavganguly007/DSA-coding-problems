# code -> https://leetcode.com/problems/maximal-square/
# src -> neetcode vdo


class Solution:
  # Recurrsive approach
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        mp = {}
        def helper(r,c):
            if r >= row or c >= col:
                return 0

            if (r,c) not in mp:
                down = helper(r+1, c)
                right = helper(r, c+1)
                diagonal = helper(r + 1, c+ 1)

                mp[(r,c)] = 0
                if matrix[r][c] == "1":
                    mp[(r,c)] = 1 + min(down, right, diagonal)
            
            return mp[(r,c)]
        helper(0,0)

        return max(mp.values()) ** 2
        
