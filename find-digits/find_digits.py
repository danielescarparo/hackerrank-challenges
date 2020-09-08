#!/bin/python3
# Find Digits https://www.hackerrank.com/challenges/find-digits/problem

import math
import os
import random
import re
import sys


def findDigits(n):
    divisorTotal = 0
    number = str(n)

    for digit in number:
        if (int(digit) > 0):
            rest = int(number) % int(digit)
            if rest == 0:
                divisorTotal += 1

    return divisorTotal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
