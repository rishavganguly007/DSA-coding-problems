#code: https://leetcode.com/problems/string-compression-iii/

class Solution:
    def compressedString(self, word: str) -> str:
        p1, p2 = 0, 1
        comp = ""
        count = 1
        for _ in range(len(word)):
            if p2 >= len(word):
                comp+= str(count)+word[p1]
                break
            if word[p1] == word[p2] and count < 9:
                count+=1
                p2+=1
            elif count == 9:
                comp += str(count) + word[p1]
                p1 = p2
                count = 1
                p2+=1
            else:
                comp += str(count) + word[p1]
                p1 = p2
                count = 1
                p2+=1
        return comp

        
