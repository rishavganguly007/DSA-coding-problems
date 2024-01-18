# code : https://leetcode.com/problems/minimum-moves-to-reach-target-score/description/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0:
            return target -1
        temp = target
        steps = 0
        for i in range(maxDoubles):
            if temp == 1:
                return steps
            
            if temp % 2 != 0:
                temp -= 1
                steps += 1
            temp = int(temp/2)
            steps += 1
        return temp + steps -1
            
        
