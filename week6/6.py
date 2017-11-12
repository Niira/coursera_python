m = int(input())
mList = []
tempmList = list(map(int, input().split()))
for i in range(m):
   citydata = (i + 1, tempmList[i])
   mList.append(citydata)
n = int(input())
nList = []
tempnList = list(map(int, input().split()))
for i in range(n):
   bunkerdata = (i + 1, tempnList[i])
   mList.append(bunkerdata)

