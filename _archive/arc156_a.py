T = int(input())
NS = []
for _ in range(T):
    n = int(input())
    S = list(input())
    NS.append(tuple([n, S]))

for t in range(T):
    n = NS[t][0]
    S = NS[t][1]
    swi = False
    cnt = 0
    num = 0
    for i in range(n):
        if num >= n:
            break
        if S[num] == '0':
            num += 1
            continue
        swi = True
        if num + 1 >= n:
            break
        if S[num + 1] == '1':
            cnt += 1
            num += 2
            swi = False
            continue
        if num + 2 >= n:
            break
        if S[num + 2] == '1':
            cnt += 1
            num += 3
            swi = False
            continue
        break
    if swi:
        print(-1)
        continue
    print(cnt)
