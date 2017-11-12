fin = open('input.txt', 'r', encoding='utf8')
lines = fin.readlines()


class Man:
    last_name = ''
    first_name = ''
    first_mark = 0
    second_mark = 0

peopleList = []
for line in lines:
    tempManData = line.split()
    man = Man()
    man.last_name = tempManData[0]
    man.first_name = tempManData[1]
    man.first_mark = int(tempManData[2])
    man.second_mark = int(tempManData[3])
    peopleList.append(man)

peopleList.sort(key=lambda man: man.last_name)
fout = open('output.txt', 'w', encoding='utf8')
for man in peopleList:
    print(man.last_name, man.first_name, man.second_mark, file=fout)
fin.close()
fout.close()
