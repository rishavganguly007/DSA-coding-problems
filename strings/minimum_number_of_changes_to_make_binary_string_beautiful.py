# code: https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/
class Solution:
    # res : https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/solutions/6008345/beats-100-00-for-loop-explained-with-example
    def minChanges(self, s: str) -> int:
        count = 0
        for i in range(0,len(s)-1, 2):
            if s[i] != s[i+1]:
                count += 1
        return count
        
