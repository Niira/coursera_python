def ReduceFraction(n, m):
    global p
    global q
    global i
    while i != 0:
        i = q and ReduceFraction(p, q % p) or p
    return n // i, m // i


n = int(input())
m = int(input())
i = 1
q = m
p = n
print(ReduceFraction(n, m))
