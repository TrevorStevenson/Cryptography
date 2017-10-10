#!/usr/bin/env python3

def gcd(a, b):
    if a < b:
        t, a = a, b
        b = t

    if b == 0:
        return a
    return gcd(b, a % b)

def extended_gcd(a, b):
    u, g, x, y = 1, a, 0, b

    while y != 0:
        q = g // y
        t = g % y
        s = u - q * x
        u, g, x, y = x, y, s, t

    if b == 0:
        return g, u, 0

    if u <= 0:
        u %= b // g

    v = (g - a * u) // b

    return g, u, v

def inverse(x, p):
    g, u, v = extended_gcd(x, p)
    return u

if __name__ == "__main__":
    print("A: ", end="")
    a = int(input())
    print("B: ", end="")
    b = int(input())
    if a == 0 and b == 0:
        print("The GCD is not defined.")
    else:
        g, u, v = map(str, extended_gcd(a, b))
        print("The GCD is " + g)
        print(str(a) + "*"+ u + " + " + str(b) + "*" + v + " = " + g)
