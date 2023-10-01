# code -> https://leetcode.com/problems/group-anagrams/
# resource -> https://www.youtube.com/watch?v=vzdNOK2oB2E
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()

        
