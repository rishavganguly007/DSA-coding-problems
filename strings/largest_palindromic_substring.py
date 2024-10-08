# code -> https://leetcode.com/problems/longest-palindromic-substring/submissions/
# soruce -> neetcode

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # start from the middle and expand
        res = ""
        resLen = 0
        res_l, res_r = 0, 0
        n = len(s)
        for i in range(n):

            # odd length

            l, r = i, i 

            while l >=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    res_l, res_r = l, r 
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l,r = i, i+1

            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res_l, res_r = l, r
                    resLen = r - l + 1
                l -= 1
                r += 1
        
        return s[res_l : res_r+1]
