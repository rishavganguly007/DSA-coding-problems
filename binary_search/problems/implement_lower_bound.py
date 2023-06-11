# problem -> https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1
# resource -> https://youtu.be/6zhGS79oQ4k

def findFloor(self,A,N,X):
        #Your code here
        low = 0
        high = N - 1
        store = -1
        while (low <= high):
            mid = math.floor((low + high) / 2)
            if X >= A[mid]:
                store = mid
                low = mid +1
            else:
                high = mid - 1
           
                
        return store
print(findFloor([1 ,2 ,8 ,10 ,11, 12, 19], 7, 0))
      
