# code -> https://practice.geeksforgeeks.org/problems/search-insert-position-of-k-in-a-sorted-array/1

def searchInsertK(self, Arr, N, k):
        # code here
        high = N-1
        low = 0
        ans = N
        
        while low <= high:
            mid = math.floor( (high + low) / 2)
            if Arr[mid] >= k:
                ans = mid
                high = mid -1
            else:
                low = mid + 1
                
        return ans
