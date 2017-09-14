def power(a, n):
    global i
    if i % 2 != 0:
        if n == 0:
            return 1
        return a * power(a, n-1)
    else:
        if n == 0:
            return 1
        return a * a * power(a, n - 2)


a = float(input())
n = int(input())
i = n
print(power(a, n))
