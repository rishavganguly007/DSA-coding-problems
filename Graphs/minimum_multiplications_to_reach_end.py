# code : https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/
# resource : https://takeuforward.org/graph/g-39-minimum-multiplications-to-reach-end/



from typing import List
from queue import Queue
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        if start == end:
            return 0
        mod = 100000
        q = Queue()
        q.put((0, start)) # initial dist, start
        dist = [float('inf')] * mod
        dist[start] = 0
        
        while not q.empty():
            steps, node = q.get()
            
            for it in arr:
                val = (node * it) % mod
                
                if steps + 1 < dist[val]:
                    dist[val] = steps + 1
                    
                    if val == end:
                        return steps + 1
                    q.put((steps+1, val))
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends

