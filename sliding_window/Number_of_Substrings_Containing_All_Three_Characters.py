# code: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# resource: https://www.youtube.com/watch?v=xtqN4qlgr8s&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=8
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mp = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        for i in range(len(s)):
            mp[s[i]] = i
            if mp['a'] != -1 and mp['b'] != -1 and mp['c'] != -1:
                count += 1 + min(mp['a'], mp['b'], mp['c'])

        return count 
                
        
