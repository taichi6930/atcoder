import math

n = int(input())
listN = []

for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        listN.append(i)
        if i != n//i:
            listN.append(n // i)
listN.sort()
for i in range(len(listN)):
    print(listN[i])
