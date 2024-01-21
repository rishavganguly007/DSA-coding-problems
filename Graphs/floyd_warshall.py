# code : https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1
# resource : https://takeuforward.org/data-structure/floyd-warshall-algorithm-g-42/
class Solution:
	def shortest_distance(self, matrix):
		#Code here
		n = len(matrix)
		for i in range(n):
		    for j in range(n):
		        if matrix[i][j] == -1:
		            matrix[i][j] = 10 **9 
		        if i == j:
		            matrix[i][j] == 0
		 
		for k in range(n):
		    for i in range(n):
		        for j in range(n):
		            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
		
	    # to check -ve cycle
	    
	    for i in range(n):
	        for j in range(n):
	            if i==j and matrix[i][j] < 0:
	                # return [-1]
	                pass
		            
		for i in range(n):
		    for j in range(n):
		        if matrix[i][j] == 10 **9:
		            matrix[i][j] =  -1
		        
    
        return matrix
