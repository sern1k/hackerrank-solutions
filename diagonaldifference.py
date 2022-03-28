import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    lefttoright = 0
    righttoleft = 0
    for i in range(len(arr)):
        lefttoright += arr[i][i]
        righttoleft += arr[i][len(arr)-1-i]

    return abs(lefttoright-righttoleft)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
