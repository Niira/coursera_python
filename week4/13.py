def sum(a, b):
    global i
    if i == b == 0:
        return a
    elif i != 0 and b == 0:
        return 1
    else:
        i += 1
        return a + sum(1, b - 1)


a = int(input())
b = int(input())
i = 0
print(sum(a, b))
