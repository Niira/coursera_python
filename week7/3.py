f_input = set(map(int, input().split()))
s_input = set(map(int, input().split()))
print(*sorted(list(f_input & s_input)))
