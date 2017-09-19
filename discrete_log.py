#!/usr/bin/env python3

import math
import euclidean

def discrete_log(g, h, p):
    # Initialize list 1
    # as a hash table for O(1) lookup
    # Keys are the powers of g and values are the exponent.
    powers_of_g = {}

    # The order is p-1
    n = 1 + math.floor(math.sqrt(p-1))
    inv_pwrs = []

    # Build list 1 and 2 and lookup items from list 2 in list 1
    for i in range(0, n+1):
        pwr = pow(g, i, p)
        powers_of_g[str(pwr)] = i
        inv_power = ( h * euclidean.inverse(pow(g, n * i, p), p) ) % p
        if str(inv_power) in powers_of_g:
            print(powers_of_g[str(inv_power)] + i * n)
            return
        inv_pwrs.append(inv_power)

    # If match was not found, traverse the list again
    # as both lists are now fully built
    for i in range(n):
        if str(inv_pwrs[i]) in powers_of_g:
            print(powers_of_g[str(inv_pwrs[i])] + i * n)
            return

if __name__ == "__main__":
    print("g: ", end="")
    g = int(input())
    print("h: ", end="")
    h = int(input())
    print("p: ", end="")
    p = int(input())
    discrete_log(g, h, p)
