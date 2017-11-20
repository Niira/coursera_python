SandN = list(map(int, input().split()))
users = []
while len(users) != SandN[1]:
    users.append(int(input()))

users.sort()
count = 0
i = 0

while SandN[0] >= 0:
    SandN[0] -= users[i]
    i += 1
    count += 1

if SandN[0] < 0:
    print(count - 1)
else:
    print(count)
