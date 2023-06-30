# code -> https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
# resource -> https://www.youtube.com/watch?v=Z0hwjftStI4
class Solution:
    
    #Function to find minimum number of pages.
    def findStudents(self, A, N, pages):
        stud = 1
        studPages = 0
        for i in range(N):
            if studPages + A[i] <= pages:
                studPages += A[i]
            else:
                stud += 1
                studPages = A[i]
        return stud
            
    def findPages(self,A, N, M):
        #code here
        if M > N:
            return -1
        low = max(A)
        high = sum(A)
        
        while low <= high:
            mid = (low + high) // 2
            no_of_stud = self.findStudents(A, N, mid)
            if  no_of_stud > M:
                low = mid + 1
            else:
                high = mid - 1
                
        return low
