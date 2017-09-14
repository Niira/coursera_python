cell11 = int(input())
cell12 = int(input())
cell21 = int(input())
cell22 = int(input())
step1 = cell11 - cell21
step2 = cell12 - cell22
if step1 == 0 and step2 == 0:
    print('NO')
elif -1 <= step1 <= 1 and -1 <= step2 <= 1:
    print('YES')
else:
    print('NO')
