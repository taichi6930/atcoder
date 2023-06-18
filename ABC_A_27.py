lList = list(map(int, input().split()))
a = []
b = []
a.append(lList[0])
b.append(1)
for l in range(1, 3):
    cnt = 0
    for k in range(len(a)):
        if a[k] == lList[l]:
            b[k] += 1
            cnt += 1
    if(cnt == 0):
        a.append(lList[l])
        b.append(1)
for l in range(len(a)):
    if b[l] % 2 == 1:
        print(a[l])
