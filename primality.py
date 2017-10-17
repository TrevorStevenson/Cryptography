#!/usr/bin/env python3

def is_prime(n):
    for i range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True