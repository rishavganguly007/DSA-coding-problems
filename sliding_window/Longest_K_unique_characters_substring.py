# code : https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
# resource : https://www.youtube.com/watch?v=teM9ZsVRQyc&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=6

#User function Template for python3
from collections import defaultdict 
class Solution:

    def longestKSubstr(self, s, k):
        # code here
        l,r, maxlen = 0, 0, 0
        seq = defaultdict(int)
        
        while(r < len(s)):
            seq[s[r]] += 1
            
            if len(seq) > k:
                seq[s[l]] -= 1
                if seq[s[l]] == 0:
                    seq.pop(s[l])
                l +=1
            
            if len(seq) <= k:
                maxlen = max(maxlen, r - l + 1)
            r += 1
        if len(seq) < k:
            return -1
        return maxlen


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends
