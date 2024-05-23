# code: https://leetcode.com/problems/longest-repeating-character-replacement/
# resource : https://www.youtube.com/watch?v=_eNhaDCr6P0&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=8
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, maxLen, maxFreq = 0, 0 , 0, 0
        mp = defaultdict(int)

        while r < len(s):
            mp[s[r]] += 1
            maxFreq = max(maxFreq, mp[s[r]])

            if (r-l+1) - maxFreq > k:
                mp[s[l]] -= 1
                maxfreq = 0 # reset and to find the max freq in new sliding window
                l += 1
            if (r-l+1) - maxFreq <= k:
                maxLen = max(maxLen, r-l+1)
            r += 1
        return maxLen
