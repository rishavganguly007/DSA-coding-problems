from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

	# Your code here
    # return the answer
    maxi = arr[0]
    sum = 0
    for i in range(n):
        sum += arr[i]
        if sum < 0:
            sum = 0
        maxi = max(maxi, sum) 
    return maxi

val = maxSubarraySum([1,3,-4,3,-2,-7], 6)
print(val)
