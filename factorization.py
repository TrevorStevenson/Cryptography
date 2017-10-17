#!/usr/bin/env python3

import euclidean as e
import primality as p

def pMinusOne(n):
    a = 2
    for i in range(2, 2*n):
        a = pow(a, i, n)
        gcd = euclidean.gcd(a-1, n)
        if gcd < n and gcd > 1:
            return gcd

def quadratic_sieve(n, low, high, b):
    sieve = [ i**2 - n for i in range(low, high+1) ]
    powers = set()

    for i in range(2, b+1):
        if p.is_prime(i):
            powers.add(i)

    for pwr in powers:
        for i, s in enumerate(sieve):
            while s % pwr == 0:
                s[i] //= pwr

    return sieve