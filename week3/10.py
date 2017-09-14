a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
if D == 0:
    xplus = (- b + D ** 0.5) / (2 * a)
    print(xplus)
elif D > 0:
    xminus = (- b - D ** 0.5) / (2 * a)
    xplus = (- b + D ** 0.5) / (2 * a)
    if xplus > xminus:
        print(xminus, xplus)
    else:
        print(xplus, xminus)
