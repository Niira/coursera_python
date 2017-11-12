N = int(input())
InputList = list(map(int, input().split()))
X = int(input())
b = [abs(InputList[i] - X) for i in range(N)]
print(InputList[b.index(min(b))])
