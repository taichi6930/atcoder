n = int(input())
s = input()
alphaList = "qwertyuiopasdfghjklzxcvbnm"
sMax = 0
for i in range(1, n):
    sSum = 0
    for j in range(26):
        if s[0:i].count(alphaList[j]) > 0 and s[i:n].count(alphaList[j]) > 0:
            sSum += 1
    sMax = max(sMax, sSum)
print(sMax)
