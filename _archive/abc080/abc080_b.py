n = input()
nList = list(n)
nSum = 0
for i in range(len(n)):
    nSum += int(nList[i])

print("Yes" if int(n) % nSum == 0 else "No")
