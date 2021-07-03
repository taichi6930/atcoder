s = input()
sMin = 1000
for i in range(len(s) - 2):
    sStr = abs(int(s[i:i+3]) - 753)
    if sStr < sMin:
        sMin = sStr
print(sMin)
