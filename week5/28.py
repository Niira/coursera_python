N = int(input())
InputList = list(map(int, input().split()))
X = int(input())
ymin = 1001
for i in range(N):
    y = abs(InputList[i] - X)
    if y < ymin:
        ymin = y
        Answer = InputList[i]
        if ymin == 0:
            break
print(Answer)
