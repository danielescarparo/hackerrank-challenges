#!/bin/python3
# Save the Prisoner! https://www.hackerrank.com/challenges/save-the-prisoner/problem

import math
import os
import random
import re
import sys


def saveThePrisoner(chairs, sweets, start):
    leftOver = sweets % chairs
    if leftOver == 0 and start == 1:
        return chairs
    people = (start + leftOver - 1) % chairs
    if people == 0:
        return chairs
    return people


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
