def MinDivisor(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return i
    return n

n = int(input())
print(MinDivisor(n))
