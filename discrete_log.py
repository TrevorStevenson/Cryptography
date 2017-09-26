#!/usr/bin/env python3

import math
import euclidean

def discrete_log(g, h, p):
    # Initialize list 1 as a hash table for O(1) lookup.
    # Keys are the powers of g and values are the exponent.
    powers_of_g = {}

    # The order is p-1.
    n = 1 + math.floor(math.sqrt(p-1))
    inv_pwrs = []

    # Build list 1 and 2 and lookup items from list 2 in list 1
    # For large p, it takes too long to completely build
    # list 1 first. So the lists are built simultaneously and
    # lookup is therefore only backwards in the list.
    for i in range(0, n+1):
        pwr = pow(g, i, p)
        powers_of_g[str(pwr)] = i
        inv_power = ( h * euclidean.inverse(pow(g, n * i, p), p) ) % p
        if str(inv_power) in powers_of_g:
            print(powers_of_g[str(inv_power)] + i * n)
            return
        inv_pwrs.append(inv_power)

    # Since lookup before was only backwards, it is possible
    # to not find a match. The lists are now fully built,
    # so traverse the list again.
    for i in range(n):
        if str(inv_pwrs[i]) in powers_of_g:
            print(powers_of_g[str(inv_pwrs[i])] + i * n)
            return

def order(n, p):
    for i in range(1, p):
        if pow(n, i, p) == 1:
            print(i)
            return

def factor(n):
    factors = []
    max_val = int(math.sqrt(n))
    i = 2
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n /= i
        else:
            i += 1
    print(factors)

if __name__ == "__main__":
    print("g: ", end="")
    g = int(input())
    print("h: ", end="")
    h = int(input())
    print("p: ", end="")
    p = int(input())
    discrete_log(g, h, p)
