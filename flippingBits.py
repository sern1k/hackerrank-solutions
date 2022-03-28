import math
import os
import random
import re
import sys


def flippingBits(n):
    binary = ['0' for i in range(32)]
    bN = "{0:b}".format(n)
    for i in range(len(bN)):
        binary[31 - i] = bN[len(bN) - 1 - i]

    for i in range(32):
        if binary[i] == '0':
            binary[i] = '1'
        else:
            binary[i] = '0'

    return int(''.join(binary), 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
