cell11 = int(input())
cell12 = int(input())
cell21 = int(input())
cell22 = int(input())
step1 = cell11 - cell21
step2 = cell12 - cell22
if (abs(step1) % 2 == 0 and step2 == 0):
    print('YES')
elif (abs(step2) % 2 == 0 and step1 == 0):
    print('YES')
elif (step1 % 2 == 0 and step2 % 2 == 0):
    print('YES')
elif (step1 % 2 != 0 and step2 % 2 != 0):
    print('YES')
else:
    print('NO')
