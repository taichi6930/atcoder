import sys
import datetime
import collections
import math
from itertools import accumulate  # 累積和を求めるときに使う
from itertools import permutations  # 順列全探索で使う
from bisect import bisect_left
from pprint import pprint

from copy import copy

sys.setrecursionlimit(10000)


class ABC:
    c = [['.' for _ in range(401)] for _ in range(401)]
    ans = 200 ** 2

    def dfs(self, x, y, cnt=None, c=None):
        if not(0 <= x <= 400) or not(0 <= y <= 400) or c[y][x] == "#":
            # 壁に当たるか、探索範囲外になった時は処理を終わらせる
            return
        # print(x, y)

        if c[y][x] == "g":
            # ゴールに到達した時はYesを出力して終了
            if self.ans >= cnt:
                self.ans = cnt
                print(self.ans)
            return
        cnt += 1
        if cnt > 40:
            return

        c[y][x] = "#"  # 同じ場所を探索しないように#を入れる
        self.dfs(x + 1, y + 1, cnt, c=copy(c))
        self.dfs(x, y + 1,  cnt, c=copy(c))
        self.dfs(x - 1, y + 1,  cnt, c=copy(c))
        self.dfs(x + 1, y,  cnt, c=copy(c))
        self.dfs(x - 1, y,  cnt, c=copy(c))
        self.dfs(x, y - 1,  cnt, c=copy(c))

    def __init__(self):
        # 障害物のあるマス = n, ゴールのマスを x ,y として取得
        n, x, y = map(int, input().split())
        # (0,0) -> (200,200) に平行移動
        sx, sy = 200, 200

        self.c[200 + y][200 + x] = 'g'

        # 障害物を作成する
        for _ in range(n):
            a, b = map(int, input().split())
            self.c[b + 200][a + 200] = '#'
        self.dfs(sx, sy, cnt=0, c=copy(self.c))
        print(self.ans)


if __name__ == '__main__':
    ABC()
