n = list(map(int, input().split()))
m = [n[i] for i in range(0, len(n)) if n[i] > 0]
print(len(m))
