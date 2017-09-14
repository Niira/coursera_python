i = 1
a = -(10 ** 10)
while i != 0:
    i = int(input())
    if i == 0:
        break
    elif i > a:
        a = i
    else:
        a = a
print(a)
