# code -> https://leetcode.com/problems/backspace-string-compare

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if s == "#" and t == "#":
        #     return True
        # elif (s == "#" and t != "#") or (s != "#" and t == "#"):
        #     return False
        st1 = []
        st2 = []
        s1 = ""
        s2 = ""

        for i in s:
            if i == "#":
                if st1:
                     st1.pop()           
            else:
                st1.append(i)
        
        for i in t:
            if i == "#":
                if st2:
                    st2.pop()
            else:
                st2.append(i)
               
        return st1 == st2
        # if len(st1) != len(st2):
        #     return False
        
        # for i in range(len(st1)):
        #     if st1[i] != st2[i]: return False
        # return True

        
        
