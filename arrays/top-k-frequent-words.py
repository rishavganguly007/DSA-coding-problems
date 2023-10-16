# code -> https://leetcode.com/problems/top-k-frequent-words/description/
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if len(words) == 0: return []
        dic = {}
        mf = 1

        for i in words:
            if dic.get(i) is None:
                dic[i] = 1
            else:
                dic[i] += 1
            mf = max(mf, dic[i])

        freq = mf
        ans = []
        
        while freq >= 1:
            tempAns = []
            for i in dic:
                if dic[i] == freq:
                    tempAns.append(i)
            tempAns = sorted(tempAns)

            for i in tempAns:
                ans.append(i)
                if len(ans) == k:
                    return ans
            freq-=1
