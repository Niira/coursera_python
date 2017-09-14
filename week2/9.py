n = int(input())
if n % 10 == 1 and n != 11:
    print(n, 'korova')
elif 12 <= n <= 15:
    print(n, 'korov')
elif 2 <= (n % 10) < 5:
    print(n, 'korovy')
else:
    print(n, 'korov')
