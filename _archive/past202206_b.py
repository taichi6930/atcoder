from collections import Counter
s = input()
ss = [s[i: i + 2] for i in range(len(s) - 1)]
cSS = Counter(ss)
maxSS = cSS.most_common()[0][1]
maxList = []
for key in list(cSS.keys()):
    if cSS[key] == maxSS:
        maxList.append(key)
print(sorted(maxList)[0])
