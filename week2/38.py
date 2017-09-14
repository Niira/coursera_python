maximum = 0
beforemax = 0
m = -1
while m != 0:
    m = int(input())
    if m > maximum and m > beforemax:
        beforemax = maximum
        maximum = m
    elif m > beforemax and m <= maximum:
        beforemax = m
print(beforemax)
