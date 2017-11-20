fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
temp_answers = fin.readlines()
answers = []
for line in temp_answers:
    line = line.split()
    answers.append(line)

n = int(answers[0][0])
answers = answers[1:-1]
for i in range(0, len(answers), 2):
    for j in range(len(answers[i])):
        answers[i][j] = int(answers[i][j])

posible_set = set(range(n + 1))

for i in range(1, len(answers), 2):
    if answers[i][0] == 'YES':
        posible_set = posible_set & set(answers[i - 1])
    else:
        for number in answers[i - 1]:
            posible_set.discard(number)

print(*posible_set, file=fout)
fin.close()
fout.close()
