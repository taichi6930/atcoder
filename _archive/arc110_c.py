n = int(input())
P = list(map(int, input().split()))
indexP = {p: i for i, p in enumerate(P)}
Q = [True for _ in range(n)]
pin = 0

ans = []

for i in range(n):
    if P[i] == i + 1:
        # そのままでOKであれば、QをFalseにして次にいく
        Q[i] = False
        continue

    # Pの入れ替えを行って、Qも更新する
    k = indexP[i + 1]
    P[i:] = [P[k]] + P[i:k] + P[k + 1:]

    ans2 = []
    for j in range(pin, k + 1):
        ans2.append(j + 1)
        Q[j] = False
    pin = k

    ans += ans2[::-1][1:]

    if P[i] == i + 1:
        # そのままでOKであれば、QをFalseにして次にいく
        Q[i] = False
        continue

    if not(Q[i]):
        # 既に使われているのであれば、-1を表示して終わり
        print(-1)
        exit()


for i in ans:
    print(i)
