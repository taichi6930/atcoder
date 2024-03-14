from collections import Counter

alphaList = list("abcdefghijklmnopqrstuvwxyz")

s = list(input())
t = list(input())
atSNum = s.count("@")
atTNum = t.count("@")
notAtSNum = 0
notAtTNum = 0
for alpha in alphaList:
    a, b = s.count(alpha), t.count(alpha)
    notAtSNum += max(0, a - b)
    notAtTNum += max(0, b - a)
print(atTNum, notAtSNum, atSNum, notAtTNum)
