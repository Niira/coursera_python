x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if y2 - y1 == 1:
    if x2 - x1 == 1:
        print('YES')
    elif x2 - x1 == -1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
