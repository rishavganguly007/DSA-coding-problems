# code -> https://leetcode.com/problems/reverse-words-in-a-string/description/
class Solution:
    def reverseWords(self, s: str) -> str:
        st = s.split()
        ss = ""
        for i in range(len(st) -1, -1, -1):
            ss += st[i] + " "
        return ss.rstrip()
