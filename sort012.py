code -> https://www.codingninjas.com/codestudio/problems/631055

def sort012(arr, n) :

	# write your code here
    # don't return anything
    count0, count1, count2 = 0, 0, 0
    for i in range(n):
        if arr[i] == 0:
            count0 += 1
        if arr[i] == 1:
            count1 += 1
        if arr[i] == 2:
            count2 += 1
    
    for i in range(count0):
        arr[i] = 0
    for i in range(count0, count0 + count1):
        arr[i] = 1
    for i in range(count0 + count1, n):
        arr[i] = 2
    print(arr)

sort012([1,0,2,0,1,2,0], 7)
