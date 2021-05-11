n = list(input())
listN = {0: 0, 1: 0, 2: 0}
for i in n:
    a = int(i) % 3
    listN[a] = (listN[a] + 2) % 3 - 1
print(listN)
if listN[2] == listN[1]:
    print(0)
elif listN[2] >= 1 and listN[1] >= 1:
    print(listN[2] + listN[1] - 2)
