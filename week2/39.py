count = 0
maximum = -1
m = -1
while m != 0:
    m = int(input())
    if m > maximum:
        maximum = m
        count = 1
    elif m == maximum:
        count += 1
print(count)
