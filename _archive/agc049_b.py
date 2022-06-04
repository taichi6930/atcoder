def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


n = int(input())
S = str2intWithArray(list(input()))
T = str2intWithArray(list(input()))

cnt = 0

for i in range(n - 1):
    print(i, cnt, S, T)
    k = n - i - 1

    # 何もいじらないようにしないといけないのでcontinueをする
    if T[k] == S[k]:
        continue

    if S[k] == 0:
        print(-1)
        exit()

    cnt += 1
    S[k - 1] = (S[k - 1] + 1) % 2
    S[k] = (S[k] + 1) % 2
    print(i, cnt, S, T)


print(cnt if T[-1] == S[-1] else -1)
