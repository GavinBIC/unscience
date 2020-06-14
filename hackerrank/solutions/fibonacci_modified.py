#!/bin/python3
#
# Problem Author: PRASHANTB1984 @ hackerrank
#     Difficulty: Medium
#           link: https://www.hackerrank.com/challenges/fibonacci-modified/problem
#
# Solution
#   Author: Byung Il Choi (choi@byung.org)
#
import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    if n == 1:
        return t1
    if n == 2 :
        return t2

    t_i = 0
    for i in range(3, n+1):
        t_i = t1 + t2 ** 2
        t1 = t2
        t2 = ti

    return t_i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
