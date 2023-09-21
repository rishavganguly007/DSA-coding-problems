class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}
        dict[s[0]] = t[0]
        for i in range(1, len(s)):
            if dict.get(s[i]) == None:
                dict[s[i]] = t[i]
            else:
                if dict[s[i]] != t[i]:
                    return False
        return True
