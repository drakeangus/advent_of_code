#!/usr/bin/env python3
from sys import argv
file = open(argv[1], 'r').readlines()

from math import lcm
def CalcButtonPresses(A, B, P):
    # Eq 0 : n x A[0] + m x B[0] = P[0]
    # Eq 1 : n x A[1] + m x B[1] = P[1]
    
    f = lcm(A[0], A[1])
    F = [ f/A[0], f/A[1] ]

    m = (F[0]*P[0] -  F[1]*P[1]) / (F[0]*B[0] - F[1]*B[1])
    n = (P[0] - m*B[0]) / A[0]
    return n,m

count = 0
import re
for line in file:
    line = line.strip()
    A_res = re.search(r'.*Button A: X\+([0-9]+), Y\+([0-9]+).*',line)
    B_res = re.search(r'.*Button B: X\+(\d+), Y\+(\d+).*',line)
    P_res = re.search(r'.*Prize: X=(\d+), Y=(\d+).*',line)
    if A_res:
        A = [ int(A_res.group(1)), int(A_res.group(2)) ]
    if B_res:
        B = [ int(B_res.group(1)), int(B_res.group(2)) ]
    if P_res:
        P = [ 10000000000000 + int(P_res.group(1)), 10000000000000 + int(P_res.group(2)) ]
        
        n,m = CalcButtonPresses(A, B, P)
        if n - int(n) == 0 and m - int(m) == 0:
            count += int(3*n + m)
        
print(count)
