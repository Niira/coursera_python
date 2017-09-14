N = int(input())
h = N // 3600 % 24
min = N % 3600 // 60
sec = N % 60
print(h, '%02d' % (min), '%02d' % (sec), sep=':')
