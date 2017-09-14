a = int(input())
b = int(input())
c = a // b
d = a % b
print('YES' * 0 ** d, 'NO' * (d ** 0 - 1 ** d), sep='')