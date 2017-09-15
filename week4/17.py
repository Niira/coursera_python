def SummOfLime(a):
    if a == 0:
        return 0
    return a + SummOfLime(int(input()))


a = int(input())
print(SummOfLime(a))
