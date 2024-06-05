# code: https://leetcode.com/problems/find-common-characters/?envType=daily-question&envId=2024-06-05

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        current = [0] * 26
        common = [0] * 26

        for i in words[0]:
            common[ord(i) - ord('a')] += 1
        for word in words[1::]:
            current = [0]*26

            for letter in word:
                current[ord(letter) - ord('a')] += 1

            for j in range(26):
                common[j] = min(common[j], current[j])
        
        res = []
        for i in range(26):
            if common[i] != 0:
                j = 0
                while j < common[i]:
                    res.append( chr(i + ord('a')) )
                    j+=1
        return res
        
