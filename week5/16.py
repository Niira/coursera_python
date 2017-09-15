n = list(map(int, input().split()))
for i in range(len(n) - 1, -1, -1):
    if n[i] == max(n):
        print(max(n), i)
        break
