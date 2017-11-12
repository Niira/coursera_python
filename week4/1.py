a = int(input())
b = int(input())
c = int(input())
d = int(input())


def min4(a, b, c, d):
    minab = min(a, b)
    mincd = min(c, d)
    minres = min(minab, mincd)
    return minres

print(min4(a, b, c, d))
