# code -> https://practice.geeksforgeeks.org/problems/ceil-the-floor2802/1

def getFloorAndCeil(arr, n, X):
    # code here
    ceil = -1
    floor = 10**9
    
    for i in range(n):
        if arr[i] >= ceil and arr[i] <= X:
            ceil = arr[i]
        if arr[i] <= floor and arr[i] >= X:
            floor = arr[i]
    
    if floor == 10**9:
        floor = -1
    return 
