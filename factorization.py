#!/usr/bin/env python3

import euclidean

def pMinusOne(n):
    a = 2
    for i in range(2, 2*n):
        a = pow(a, i, n)
        gcd = euclidean.gcd(a-1, n)
        if gcd < n and gcd > 1:
            return gcd
