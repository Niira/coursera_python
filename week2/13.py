a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    x = a
    y = b
    z = c
elif b >= a and b >= c:
    x = b
    y = a
    z = c
elif c >= a and c >= b:
    x = c
    y = a
    z = b
if a > 0 and b > 0 and c > 0:
    if x <= y + z and y <= x + z and z <= x + y:
        if x ** 2 < (y ** 2 + z ** 2):
            print('acute')
        elif x ** 2 > (y ** 2 + z ** 2):
            print('obtuse')
        elif x ** 2 == y ** 2 + z ** 2:
            print('rectangular')
    else:
        print('impossible')
else:
    print('impossible')
