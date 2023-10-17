# code -> https://www.codingninjas.com/studio/problems/frog-jump_3621012
# resource -> https://www.youtube.com/watch?v=EgG3jsGoPvQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=4

from os import *
from sys import *
from collections import *
from math import *

from typing import *

def f(arr, n):
    if n <= 0:
        return 0
    step1 = 10**7
    if n-1 >=0:
        step1 = abs(arr[n] - arr[n-1]) + f(arr, n-1)
    step2 = 10**7
    if n-2 >= 0:
        step2 = abs(arr[n] - arr[n-2] )+ f(arr, n-2)
    return min(step1, step2)
def f_dp(arr, n, dp):
    if n <= 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    step1 = 10**7
    step2 = 10**7
    if n-1 >= 0:
        step1 = abs(arr[n] - arr[n-1]) + f_dp(arr, n-1, dp)
    if n-2 >= 0:
        step2 = abs(arr[n] - arr[n-2] )+ f_dp(arr, n-2, dp)
    dp[n] = min(step1, step2)
    return dp[n]

def f_tab(arr, n, dp):
    dp[0] = arr[0]
    step1 = 10 ** 7
    step2 = 10 ** 7
    for i in range(1,n):
        if i+1 <= n-1:
            step1 = abs(arr[n] - arr[i+1]) + dp[i+1]
        if i+2 <= n-1:
            step2 = abs(arr[n] - arr[i+2]) + dp[i+2]
        dp[i] = min(step1, step2)
    return dp[n-1]    
     
def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
    dp = [0]*n # set -1 if using f_dp
    #return f(heights, n-1)
    #return f_dp(heights, n-1, dp)
    return f_tab(heights, n-1, dp)
    
