# code -> https://practice.geeksforgeeks.org/problems/find-nth-root-of-m5843/1
def NthRoot(self, n, m):
		# Code here
		low = 1
		high = m
		while low <= high:
		    mid = (low + high) // 2
		    ans = mid ** n
		    if ans == m:
		        return mid
		    if ans < m:
		        low = mid + 1
		    else:
		        high = mid - 1
		return -1
