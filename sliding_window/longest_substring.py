# code -> https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if s == "":
        #     return 0
        # ans = 1
        # count = 0
        # p1, p2 = 0, 0
        # store = {}
        # while p2 < len(s):
        #     if store.get(s[p2]) is None:
        #         count+=1
        #         store[ s[p2] ] = 1
                
                
        #     else:
        #         p1 = p2 - 1
        #         p2 = p1
        #         count = 0
        #         store = {}
                
        #     p2+=1    
        #     ans = max(ans, count)
        # return ans
        mpp = [-1] * 256


        left = 0
        right = 0
        n = len(s)
        length = 0
        while right < n:
            if mpp[ord(s[right])] != -1:
                left = max(mpp[ord(s[right])] + 1, left)


            mpp[ord(s[right])] = right


            length = max(length, right - left + 1)
            right += 1
        return length
