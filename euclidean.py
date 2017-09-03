#!/usr/bin/env python3

def gcd(a, b):
    u, g, x, y = 1, a, 0, b

    while y != 0:
        q = g // y
        t = g % y
        s = u - q * x
        u, g, x, y = x, y, s, t

    if b == 0:
        return g, u, 0

    v = (g - a * u) // b

    while u <= 0:
        u, v = u + b // g, v - a // g

    return g, u, v

if __name__ == "__main__":
    print("A: ", end="")
    a = int(input())
    print("B: ", end="")
    b = int(input())
    if a == 0 and b == 0:
        print("The GCD is not defined.")
    else:
        g, u, v = map(str, gcd(a, b))
        print("The GCD is " + g)
        print(str(a) + "*"+ u + " + " + str(b) + "*" + v + " = " + g)
