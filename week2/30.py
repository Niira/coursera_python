x = int(input())
y = int(input())
i = 1
if x >= y:
    print((y + x - 1) // x)
elif x < y:
    while x + 0.1 * x <= y:
        x = x + 0.1 * x
        i = i + 1
    if y % x > 0:
        print(i + 1)
    else:
        print(i)
