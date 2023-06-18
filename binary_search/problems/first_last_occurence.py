# code -> https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1
import math
def upperBound(n, x, arr):
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

def lowerBound(n, x, arr):
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
def find(arr,n,x):
    # code here
    lb = lowerBound(n, x, arr)
    if lb == n or arr[lb] != x:
        return [-1, -1]
    return [lb, upperBound(n, x, arr) - 1]
