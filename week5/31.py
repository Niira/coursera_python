InputList = list(map(int, input().split()))
list1 = [InputList[i] for i in range(len(InputList)) if i % 2 == 0]
list2 = [InputList[i] for i in range(len(InputList)) if i % 2 != 0]
list3 = []
i = 0
if len(InputList) % 2 != 0:
    while len(list3) != len(InputList) - 1:
        list3.append(list2[i])
        list3.append(list1[i])
        i += 1
    list3.append(list1[-1])
else:
    while len(list3) != len(InputList):
        list3.append(list2[i])
        list3.append(list1[i])
        i += 1
print(*list3)
