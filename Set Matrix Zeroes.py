code-link -> https://www.codingninjas.com/codestudio/problems/set-matrix-zeros_3846774

from numpy import matrix
from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    row_len = len(matrix)
    col_len = len(matrix[0])
    col0 = -1
    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == 0:
                # mark the i-th row
                matrix[i][0] = 0

                # mark the jth col
                if j!=0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    #utilise the marked rows and cols

    for i in range(1, row_len):
        for j in range(1, col_len):
            if matrix[i][j] != 0:
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

    if matrix[0][0] == 0:
        for i in range(col_len):
            matrix[0][i] = 0
    if col0 == 0:
        for i in range(row_len):
            matrix[i][0] = 0
    print(matrix)

setZeros([[0,3,4,5,0,8,9,0,7],
          [1,3,2,3,21,5,2,0,6]])
