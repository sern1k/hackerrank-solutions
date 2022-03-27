import math
import os
import random
import re
import sys


def lonelyinteger(a):
    if len(a) == 1:
        return a[0]
    for i in range(len(a)):
        if a.count(a[i]) == 1:
            return a[i]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
