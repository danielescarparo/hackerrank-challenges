#!/bin/python3
# The Hurdle Race https://www.hackerrank.com/challenges/the-hurdle-race/problem

import math
import os
import random
import re
import sys


def hurdleRace(k, height):
    maxNumber = max(height)
    doses = maxNumber - k
    if doses >= 0:
        return doses
    else:
        return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
