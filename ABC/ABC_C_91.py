n = int(input())

listAB = [""] * n
for i in range(n):
    listAB[i] = list(map(int, input().split()))

listCD = [""] * n
for i in range(n):
    listCD[i] = list(map(int, input().split()))

print(sorted(listAB), listCD)
