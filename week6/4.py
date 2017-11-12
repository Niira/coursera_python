n = int(input())
n_list_temp = list(map(int, input().split()))
n_list = n_list_temp[: n]
m = int(input())
m_list_temp = list(map(int, input().split()))
m_list = m_list_temp[:m]
answer = []
for i in n_list:
    len_to_bunker = []
    for j in m_list:
        len_to_bunker.append(abs(i - j))
    answer.append(len_to_bunker.index(min(len_to_bunker)) + 1)
print(*answer)
