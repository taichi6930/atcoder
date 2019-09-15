s = [input() for _ in range(int(input()))]
t = [input() for _ in range(int(input()))]
yMax = 0

for i in s:
    cnt = s.count(i) - t.count(i)
    if yMax < cnt:
        yMax = cnt
print(yMax)
