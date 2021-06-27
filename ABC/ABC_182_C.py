n = list(input())
listN = {0: 0, 1: 0, 2: 0}

for i in n:
    a = int(i) % 3
    listN[a] = (listN[a] + 1) % 6

if listN[2] == listN[1]:
    print(0)
elif listN[0] == 0:
    print(-1)

print(listN)
# else:
#    print(listN[0], listN[1], listN[2])
