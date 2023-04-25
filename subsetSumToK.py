# code -> https://www.codingninjas.com/codestudio/problems/subset-sum-equal-to-k_1550954
from os import *
from sys import *
from collections import *
from math import *

def f(n, arr, k):
  if k == 0:
    return True
  if  n == 0: 
    return arr[n] == k
  notPick = f(n-1, arr, k)
  pick = False
  if arr[n] <= k:
    pick = f(n-1, arr, k - arr[n])

  return notPick or pick 

def f_dp(n, k, arr,dp):
  if k == 0:
    return True
  if  n == 0: 
    return arr[n] == k
  if dp[n][k] != -1:
    return dp[n][k]
  notPick = f_dp(n-1, k, arr, dp)
  pick = False
  if arr[n] <= k:
    pick = f_dp(n-1, k - arr[n], arr, dp)
  dp[n][k] = notPick or pick
  return dp[n][k]  

def f_tab(n, k, arr,dp):
#    dp = [[False] * k+1 for _ in range(n)]
    for i in range(n):
      dp[i][0] = True
    if arr[0] <= k:
        dp[0][arr[0]] = True

    for i in range(1,n):
      for j in range(1,k+1):
        notPick = dp[i-1][j]
        pick =  False
        if arr[i] <= j:
          pick = dp[i-1][j - arr[i]]
        dp[i][j] = notPick or pick

    return dp[n-1][k]

def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    rows = n
    cols = k
    dp = [[False] * cols for _ in range(rows)]
    return f_tab(n,k,arr, dp)
#    return f(n-1, k, arr)
#    return f_dp(n-1, k-1, arr,dp)
     
    
    
print(subsetSumToK(4, 4, [6,1,2,1])) 

