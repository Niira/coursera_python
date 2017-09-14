a = abs(int(input()))
b = abs(int(input()))
c = abs(int(input()))

x = 0

if a % 2 == 0:
    x = x + 1
elif b % 2 == 0:
    x = x + 1
elif c % 2 == 0:
    x = x + 1

if a > 0 and a % 2 == 1:
    x = x + 1
elif b > 0 and b % 2 == 1:
    x = x + 1
elif c > 0 and c % 2 == 1:
    x = x + 1

if x == 2:
    print('YES')
else:
    print('NO')
