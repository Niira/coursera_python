fin = open('input.txt', 'r', encoding='utf8')
n  = int(fin.readline())
temp = fin.read().split()
i = 0
my_list = []
while i < len(temp):
    my_list.append(temp[i + 1: i + int(temp[i]) + 1])
    i = i + int(temp[i]) + 1

print(my_list)
all_lang = set()
for student in my_list:
    all_lang.update(set((student)))
print(*list(all_lang))
