f_input = list(map(int, input().split()))
myset = set()
for number in f_input:
    if number in myset:
        print('YES')
    else:
        myset.add(number)
        print('NO')
