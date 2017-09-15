n = list(map(int, input().split()))
m = [n[i] for i in range(1, len(n)) if n[i] > n[i - 1]]
print(*m)
