# code -> https://practice.geeksforgeeks.org/problems/number-of-occurrence2259/1        
import math
class Solution:
    def upperBound(self,n, x, arr):
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = math.floor( (low + high) / 2)

            if arr[mid] > x:
                ans = mid
                high = mid - 1
            
            else:
                low = mid + 1
    
        return ans

    def lowerBound(self,n, x, arr):
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = math.floor( (low + high) / 2)

            if arr[mid] >=  x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
    
        return ans

	def count(self,arr, n, x):
		# code here
		lb = self.lowerBound(n, x, arr)
        if lb == n or arr[lb] != x:
            return 0
        return self.upperBound(n, x, arr)  - lb
