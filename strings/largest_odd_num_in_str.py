# code -> https://leetcode.com/problems/largest-odd-number-in-string/description/
class Solution:
    def largestOddNumber(self, num: str) -> str:
      '''
      start to check from the unit place, if the given position is odd, that will be 
      the largest odd num, return that
      '''
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[0: i+1] 
        return ""
