import sys
import collections
n, m = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
sc = collections.Counter(S)

ans = (n + 1) * (m + 1) * 2
sys.setrecursionlimit(10 ** 9)


def q(cnt, sPosition, tPosition):
    global S, T, ans, n, m
    # 既に回数を超えていたら終了
    if cnt >= ans:
        return

    # 全てのTを作成出来ていれば終了
    if tPosition >= m:
        ans = min(ans, cnt)
        return

    cnt += 1
    if T[tPosition] == S[sPosition]:
        tPosition += 1
        q(cnt, sPosition, tPosition)
        return

    q(cnt, (sPosition + 1) % n, tPosition)
    q(cnt, (sPosition - 1) % n, tPosition)


for a in range(m):
    if sc[T[a]] == 0:
        ans = -1
        break


q(0, 0, 0)
print(ans)


