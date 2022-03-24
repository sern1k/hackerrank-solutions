import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    arr1 = arr.copy()
    arr1.remove(min(arr1))
    maxSum = 0
    for i in range(len(arr1)):
        maxSum += arr1[i]
    arr2 = arr.copy()
    arr2.remove(max(arr2))
    minSum = 0
    for i in range(len(arr2)):
        minSum += arr2[i]

    print(minSum, maxSum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
