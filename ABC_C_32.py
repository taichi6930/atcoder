s = input()
k = int(input())
aList = []
if k <= len(s):
    for i in range(len(s) - k + 1):
        sen = s[i:i+k]
        if aList.count(sen) < 1:
            aList.append(sen)

print(len(aList))
