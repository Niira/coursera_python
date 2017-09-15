def gcd(n, m):
    return m and gcd(m, n % m) or n


def ReduceFraction(n, m):
    if gcd(n, m) > n and gcd(n, m) > m:
        return n, m
    return n // gcd(n, m), m // gcd(n, m)

n = int(input())
m = int(input())
print(ReduceFraction(n, m)[0], ReduceFraction(n, m)[1])
