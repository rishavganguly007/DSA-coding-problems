# code: https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # We start by defining a variable ans to store the
        # maximum count of elements that share the same bit position 
        # with a bit set to 1.
        ans = -1 

        # Since integers are 32 bits in length, 
        # we loop from 0 to 31 to cover all possible bit positions.
        for i in range(32):
            '''
            For each bit position i (from 0 to 31), we count how many elements in 
            candidates have that specific bit set to 1.
            
            To check if the i-th bit of a number candidate is set, 
            we use the expression candidate & (1 << i).
            1 << i shifts 1 to the i-th bit position, 
            creating a mask (like 00010000 for i = 4).
            candidate & (1 << i) checks if this bit is set by applying the mask;
            if the result is non-zero, then this bit is set in candidate
            '''
            sum = 0
            for num in candidates:
                if num & (1 << i):
                    sum += 1
            ans = max(sum, ans)
        return ans

        
