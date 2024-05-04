# code: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
# soln: https://www.youtube.com/watch?v=pBWCOCS636U

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = 0
        ans = 0
        for i in range(k):
            left += cardPoints[i]
        ans = left
        end = len(cardPoints) - 1
        j = k - 1
        for i in range(end, end - k, -1):
            left -= cardPoints[j]
            right += cardPoints[i]
            j -= 1
            ans = max(ans, left + right)
        return ans


        
