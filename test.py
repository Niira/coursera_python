# число городов
n = int(input())
n_list_temp = list(map(int, input().split()))[:n]
n_list = []
for i in n_list_temp:
    n_list.append((i, 'c'))
# число бункеров
m = int(input())
m_list_temp = list(map(int, input().split()))[:m]
m_list = []
for i in m_list_temp:
    m_list.append((i, 'b', m_list_temp.index(i) + 1))
answer = []
all_in_one = m_list + n_list
all_in_one.sort()
print(all_in_one)
for i in range(len(all_in_one)):
    if all_in_one[i][1] == 'c':
