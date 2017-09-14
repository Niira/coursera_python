a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
abc = [a, b, c]
abc.sort()
if a == b == c:
    print((3 ** 0.5 * a ** 2) / 4)
elif abc[2] ** 2 == abc[0] ** 2 + abc[1] ** 2:
    print(abc[0] * abc[1] / 2)
else:
    h = 2 / a * (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(h * a / 2)
