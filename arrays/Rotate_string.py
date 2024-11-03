# code: https://leetcode.com/problems/rotate-string/
class Solution:
    '''
The key insight is that when you concatenate a string with itself (s + s), it contains all possible rotations of the original string.

For example, if s = "abcde", then s + s = "abcdeabcde" contains all rotations: "abcde", "bcdea", "cdeab", "deabc", "eabcd".
    '''
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in s + s
