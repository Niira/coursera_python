x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if y2 - y1 > 0 and abs(y2 - y1) >= abs(x2 - x1):
    if x2 - x1 == 0 and (y2 - y1) % 2 == 0:
        print('YES')
    elif (x2 - x1) % 2 == 0 and (y2 - y1) % 2 == 0:
        print('YES')
    if (x2 - x1) % 2 != 0 and (y2 - y1) % 2 != 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
