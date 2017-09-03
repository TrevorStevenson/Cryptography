#!/usr/bin/env python3

def gcd(a, b):
    u, g, x, y = 1, a, 0, b

    while y != 0:
        q = g // y
        t = g % y
        s = u - q * x
        u, g, x, y = x, y, s, t

    return g, u, (g - a * u) // b

if __name__ == "__main__":
    print("A: ", end="")
    a = int(input())
    print("B: ", end="")
    b = int(input())
    g, u, v = map(str, gcd(a, b))
    print("The GCD is " + g)
    print(str(a) + "*"+ u + " + " + str(b) + "*" + v + " = " + g)
