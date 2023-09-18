'''
A basket can be arrenaged in either with 2-mangoes(M) and 1-Apple(A) or 1-M and 2-A

given A and M fruits find the max baskets that can be made

input:
A - no of apples
B - no of mangoes

ouput:
no of baskets

eg-1:
A = 1, M = 1
output: 0 

eg-2:
A = 5, B = 4
output: 3
Explanation: (A,A,M), (A, A, M), (A, M, M)

'''

def countBasket(A, M):
  return min(A, M, (A + M) // 3)
A = int(input())
B = int(input())
print(countBasket(A, M))
