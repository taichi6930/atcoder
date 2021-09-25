from copy import copy
import collections
from itertools import accumulate  # 累積和を求めるときに使う


def dfs(x, y, fx=None, fy=None, c=None, r=None):
    if not(0 <= x < fx) or not(0 <= y < fy):
        # 壁に当たるか、探索範囲外になった時は処理を終わらせる
        return
    r.append(c[y][x])

    if x == fx - 1 and y == fy - 1:
        r = sorted(r, reverse=True)
        ansList.append(list(accumulate(r)))
        return

    dfs(x + 1, y, fx, fy, c, copy(r))
    dfs(x, y + 1, fx, fy, c, copy(r))


ansList = collections.deque()


def main():
    h, w = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(h)]
    r = collections.deque([])
    dfs(0, 0, fx=w, fy=h, c=A, r=copy(r))

    ans = [0 for _ in range(h + w - 1)]
    for an in ansList:
        for i in range(len(an)):
            ans[i] = max(ans[i], an[i])
    for k in ans:
        print(k)


if __name__ == '__main__':
    main()
