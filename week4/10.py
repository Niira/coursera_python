def IsPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True

n = int(input())
if not IsPrime(n):
    print("NO")
else:
    print("YES")
