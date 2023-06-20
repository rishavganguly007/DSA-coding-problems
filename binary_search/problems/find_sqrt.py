# code -> https://practice.geeksforgeeks.org/problems/square-root/0
  def floorSqrt(self, x): 
    #Your code here
    
        low = 1
        high = x
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            ans = mid * mid
            if ans <= x:
                low = mid + 1
            else:
                high = mid - 1
        return high
