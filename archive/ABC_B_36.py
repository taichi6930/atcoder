n = int(input())
beforeList = []
afterList = []

for _ in range(n):
    beforeList.append(list(input()))

afterList = beforeList

print("beforeList")
for i in range(n):
    print("".join(beforeList[i]))


for i in range(n):
    for j in range(n):
        if n/2 <= i and n/2 <= j:
            afterList[n - i - 1][j] = beforeList[i][j]
            break

        if n/2 <= i and n/2 >= j:
            afterList[i][n - j - 1] = beforeList[i][j]
            break

        if n/2 >= i and n/2 <= j:
            afterList[n - i - 1][j] = beforeList[i][j]
            break

        if n/2 >= i and n/2 >= j:
            afterList[i][n - j - 1] = beforeList[i][j]
            break

print("afterList")
for i in range(n):
    print("".join(afterList[i]))
