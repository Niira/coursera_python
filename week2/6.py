x = int(input())
y = int(input())
z = y % (y - x + 1)
if z == 0:
    print('YES')
else:
    print('NO')
