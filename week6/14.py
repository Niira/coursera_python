fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
k = int(fin.readline())
lines = fin.readlines()
marks = []
for line in lines:
    person = line.split()
    mark_40 = 0
    for i in range(-3, 0):
        if int(person[i]) >= 40:
            mark_40 += 1
    if mark_40 == 3:
        marks.append(int(person[-1]) + int(person[-2]) + int(person[-3]))
if len(marks) <= k:
    print('0', file=fout)
else:
    marks.sort(key=lambda mark: -mark)
    if marks[0] == marks[k]:
        print('1', file=fout)
    else:
        if marks[k-1] != marks[k]:
            print(marks[k-1], file=fout)
        else:
            i = 1
            while marks[k-i] == marks[k]:
                i += 1
            print(marks[k-i], file=fout)
