# code -> https://leetcode.com/problems/valid-anagram/description/
class Solution:
    def create_dict(self, arr):
        dic = {}
        for i in arr:
            if dic.get(i) is None:
                dic[i] = 1
            else: 
                dic[i] += 1
        return dic
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) > len(s):
            return False
        s_dict = self.create_dict(s)
        t_dict = self.create_dict(t)

        for key, value in s_dict.items():
            if t_dict.get(key) is None:
                return False
            if t_dict[key] != value:
                return False
        return True
