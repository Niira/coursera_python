# функции вывода
print('1', '2', '3', sep=' + ', end=' ')
print('=', 1 + 2 + 3)

# математические операции
print(11 - 6)
print(11 * 6)
print(11**6) #возведение в степень
print(11 // 6) #целочисленное деление
print(11 % 6) #остаток от целочисленного деления

print((7 - 8) % 24) # как можно посчитать время

#работа с переменными на основе физической задачи
speed = 108
time = 12
dist = time * speed
print(dist)

#операции со строками
phrase = 'Hasta la vista'
who = '"baby"'
print(phrase, ', ', who, '!', sep='')

ans = 2 + 3
expr = '2 + 3 = '
print(expr + str(ans))
print(ans + 1) # строку можно str превращать в строку

#умножение строк
print("abc" * 3)

name = input()
print("Hello,", name)

a = int(input())
b = int(input())
print(a + b)
