#code: https://leetcode.com/problems/filling-bookcase-shelves/?envType=problem-list-v2&envId=50vlu3z5&difficulty=MEDIUM
# resource: neetcode.io
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [-1] * (len(books)) 
        def f(i):
            if i == len(books):
                return 0
            if dp[i] != -1:
                return dp[i]

            max_height = 0
            curr_width = shelfWidth 
            dp[i] = float('inf')
            for j in range(i, len(books)):
                width, height = books[j]

                if width > curr_width:
                    break
                curr_width -= width
                max_height = max(max_height, height)
                dp[i] = min(dp[i], f(j+1) + max_height)
            return dp[i]
        return f(0)
        
