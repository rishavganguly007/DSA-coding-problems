# code : https://www.geeksforgeeks.org/problems/alien-dictionary/1
# resource: https://www.youtube.com/watch?v=U3N_je7tWAs

from queue import Queue

class Solution:
    def topo_sort(self, v, adj):
        
        inDegree = [0] * v
        
        for i in range(v):
            for j in adj[i]:
                inDegree[j] += 1
                
        q = Queue()
        topo = []
        
        for i in range(v):
            if inDegree[i] == 0:
                q.put(i)
                
        while not q.empty():
            node = q.get()
            topo.append(node)
            
            for i in adj[node]:
                inDegree[i] -= 1
                if inDegree[i] == 0:
                    q.put(i)
        
        return topo
        
        
        
        
        
    def findOrder(self,alien_dict, N, K):
    # code here
        adj = [[] for _ in range(K)]
        
        '''
        match 2 strings for the order, for eg, 
        
        abcd
        abce, therefore d -> e, as abc is same
        
        '''
        
        for i in range(N - 1):
            str1 = alien_dict[i]
            str2 = alien_dict[i+1]
            
            sz = min(len(str1), len(str2))
            
            for j in range(sz):
                if str1[j] != str2[j]:
                    # for eg, ord('a') - ord('a') is 0
                    adj[ord(str1[j]) - ord('a')].append(ord(str2[j]) - ord('a'))
                    break
                
        topo =  self.topo_sort(K, adj)
        
        ans = ""
        
        for i in topo:
            ans += chr(i + ord('a'))
        
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3
class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
