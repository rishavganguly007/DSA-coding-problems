#code -> https://www.codingninjas.com/codestudio/problems/873366
from typing import List
def find_missing_repeating(arr: List[int]) -> List[int]:
    # Will hold xor of all elements and numbers from 1 to n
    xor1 = arr[0]


    # Will have only single set bit of xor1
    set_bit_no = 0


    # Get the xor of all array elements
    for i in range(1, len(arr)):
        xor1 = xor1 ^ arr[i]


    # XOR the previous result with numbers from 1 to n
    for i in range(1, len(arr) + 1):
        xor1 = xor1 ^ i


    # Get the rightmost set bit in set_bit_no
    set_bit_no = xor1 & ~(xor1 - 1)


    # Now divide elements into two sets by comparing a rightmost set bit
    # of xor1 with the bit at the same position in each element.
    # Also, get XORs of two sets. The two XORs are the output elements.
    # The following two for loops serve the purpose
    x = 0
    y = 0
    for i in range(len(arr)):
        if arr[i] & set_bit_no:
            # arr[i] belongs to first set
            x = x ^ arr[i]
        else:
            # arr[i] belongs to second set
            y = y ^ arr[i]


    for i in range(1, len(arr) + 1):
        if i & set_bit_no:
            # i belongs to first set
            x = x ^ i
        else:
            # i belongs to second set
            y = y ^ i


    # NB! numbers can be swapped, maybe do a check ?
    x_count = 0
    for i in range(len(arr)):
        if arr[i] == x:
            x_count += 1


    if x_count == 0:
        return [y, x]


    return [x, y]

pp = [2,3,3,4,1]
n = len(arr)
miss, repeat = find_missing_repeating(pp )

print(miss, repeat)
