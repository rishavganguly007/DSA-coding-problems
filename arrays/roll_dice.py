'''
Code

Given N dices each face ranging from 1 to 6, return the minimum number of rotations necessary for each dice show the same face.

Notice in one rotation you can rotate the dice to the adjacent face.

For example, you can rotate the dice shows 1 to show 2, 3, 4, or 5. But to make it show 6, you need two rotations.

Input
The input consists of three arguments:

N: a list of integer represent dices each face ranging from 1 to 6

Output
return the minimum number of rotations necessary for each dice show the same face

Examples
Example 1:
Input:
N = [6, 5, 4]

Output: 2
Example 2:
Input:
N = [6, 6, 1]

Output: 2
Example 3:
Input:
N = [6, 1, 5, 4]

Output: 3

'''

from typing import List

def calculate_rotation_cost(dice_value: int, target: int) -> int:
    if dice_value == target:
        return 0
    elif dice_value + target == 7:
        return 2
    else:
        return 1

def number_of_rotations(dice: List[int]) -> int:
    min_rotations = float('inf')
    for target in range(1, 7):
        rotations = sum(calculate_rotation_cost(dice_value, target) for dice_value in dice)
        min_rotations = min(min_rotations, rotations)
    return min_rotations

if __name__ == '__main__':
    dice = [int(x) for x in input().split()]
    res = number_of_rotations(dice)
    print(res)
