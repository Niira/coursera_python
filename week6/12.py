fin = open('input.txt', 'r', encoding='utf8')
n = int(fin.readline())
lines = fin.readlines()
people = []
for i in range(len(lines)):
    line = lines[i].split()
    people.append((-int(line[1]), line[0]))

people.sort()
for person in people:
    print(person[1])
