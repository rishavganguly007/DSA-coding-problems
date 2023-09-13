# code -> https://www.codingninjas.com/studio/problems/row-of-a-matrix-with-maximum-ones_982768

def findLowerBoundOf1(arr,m):
    low = 0
    high = m - 1

    while low <= high:
        mid = ( low + high ) // 2
        if arr[mid] != 1:
            low = mid + 1
        else:
            high = mid - 1
    return low

def findTotal1(arr, m):
    k = findLowerBoundOf1(arr,m)
    if k == m:
        return 0
    return m - k

def rowWithMax1s(matrix: [[int]], n: int, m: int) -> int:
    index = -1
    k = 0

    for i in range(n):
        temp = findTotal1(matrix[i], m)
        if temp > k:
            k = temp
            index = i
    return index


"""
n = 3 m = 3
1  1  1
0  0  1
0  0  0
Sample Output 1 :
0
"""
