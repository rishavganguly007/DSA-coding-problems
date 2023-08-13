'''
Geek has N bricks. He needs to build a staircase consisting of k rows where the ith row has exactly i bricks. If he starts from the first row, find the number of complete rows of the staircase that he will be able to build completely.
Example 1:
Input:
N: 5
Output: 2
Explanation: 
Row 1: X
Row 2: X X
Row 3: X X
Only 2 rows are complete.

Example 2:
Input:
N: 8
Output: 3
Explanation:
X
X X
X X X
X X
Only 3 rows are complete.

Your Task:
You dont need to read input or print anything. Your task is to complete the function completeRows() which takes integer n as input parameter and returns the number of complete rows possible.

Constraints:
1 <= n <= 109


'''


class Solution:
    def completeRows(self, n : int) -> int:
        # code here
        if n == 0:
            return 0
        y = 1
        while(1):
            s = (y * (y + 1)) / 2
            if s == n:
                return y
            if s > n:
                return y - 1
            y += 1
