n = input()
nStrSum = 0
for i in range(len(n)):
    nStrSum += int(n[i])
print("Yes" if int(n) % nStrSum == 0 else "No")
