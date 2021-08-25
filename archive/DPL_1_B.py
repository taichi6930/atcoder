from pprint import pprint
import datetime
from functools import reduce
from operator import mul
import collections
import math
from itertools import accumulate  # 累積和を求めるときに使う
from itertools import permutations  # 順列全探索で使う
from bisect import bisect_left


def main():
    # ナップザックDP
    N, W = map(int, input().split())  # n:品物の数 w:容量
    vw = [None for _ in range(N)]  # vw: 荷物の価値と重さが入っている
    vw_wtotal = 0
    for a in range(N):
        v, w = map(int, input().split())
        vw_wtotal += w
        vw[a] = {'v': v, 'w': w}

    # 箱の用意をする（箱の大きさはもっとアバウトでもいい？）
    dp = [[None for a in range(W + 1)] for b in range(N + 1)]

    # 初期値を入力する
    for b in range(W + 1):
        dp[0][b] = 0
    for i in range(N):
        v, w = vw[i]['v'], vw[i]['w']
        for j in range(W + 1):
            if j - w < 0:
                dp[i + 1][j] = dp[i][j]
                continue
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w] + v)

    print(dp[N][W])


if __name__ == '__main__':
    main()
