#code -> https://leetcode.com/problems/longest-common-prefix/

    def longestCommonPrefix(self, strs: List[str]) -> str:
        t: tuple = tuple(zip(*strs))
        ch = ""
        for var in t:
            if len(set(var)) == 1:
                ch += var[0]
            else:
                return ch
        return ch
