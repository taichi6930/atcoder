s = input()
abcList = "abcdefghijklmnopqrstuvwxyz"
swi = "None"
for i in range(len(abcList)):
    if s.count(abcList[i]) == 0:
        swi = abcList[i]
        break
print(swi)
