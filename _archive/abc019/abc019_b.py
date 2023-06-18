s = list(input())
tList = [s[0]]
tNumList = [1]
t = ""

for i in range(1, len(s)):
    if tList[len(tList)-1] == s[i]:
        tNumList[len(tList)-1] += 1
    else:
        tList.append(s[i])
        tNumList.append(1)

for i in range(0, len(tList)):
    t += (tList[i] + str(tNumList[i]))

print(t)
