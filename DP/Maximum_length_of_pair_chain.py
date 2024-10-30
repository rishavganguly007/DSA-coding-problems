# code-> https://leetcode.com/problems/maximum-length-of-pair-chain/?envType=problem-list-v2&envId=50vlu3z5&difficulty=MEDIUM

class Solution:

'''
   (2,3)  (5,6)
   .__.  .__.
 (1,8)
.______________.
--------------------------------->


sorting it based on the end will opimese it
'''


    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda p:p[1])

        longest = 1
        end = pairs[0][1]
        for i in range(1, len(pairs)):
            if pairs[i][0] > end:
                longest += 1
                end = pairs[i][1]
        return longest

        
