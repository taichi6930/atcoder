from pprint import pprint
import collections
import sys


class Main:
    def __init__(self):
        self.h, self.w = map(int, input().split())
        self.c = [list(input()) for i in range(self.h)]
        self.cnt = self.c.count('#')
        self.d = [[None for i in range(self.w)] for j in range(self.h)]
        self.e = collections.deque()

        self.main()

    def dfs(self, x, y):
        if not(0 <= x < self.h) or not(0 <= y < self.w) or self.d[x][y] == ".":
            # 壁に当たるか、探索範囲外になった時は処理を終わらせる
            self.e.pop()
            return
        print(self.e)
        if self.d[x][y] == "g" and len(self.e) == self.cnt - 1:
            # ゴールに到達した時はYesを出力して終了
            print(self.e)
            sys.exit()

        self.d[x][y] = "."  # 同じ場所を探索しないように#を入れる
        self.e.append([x, y])
        self.dfs(x + 1, y)
        self.dfs(x - 1, y)
        self.dfs(x, y + 1)
        self.dfs(x, y - 1)

    def main(self):
        # スタート位置を決める
        for i in range(self.h):
            for j in range(self.w):
                if self.c[i][j] == ".":
                    continue

                for k in range(self.h):
                    for l in range(self.w):
                        self.e = collections.deque().copy()
                        for a in range(self.h):
                            for b in range(self.w):
                                self.d[a][b] = self.c[a][b]
                        self.d[i][j] = "s"
                        self.e.append([i, j])
                        if self.d[k][l] == "." or self.d[k][l] == "s":
                            continue
                        self.d[k][l] = "g"
                        self.dfs(i, j)
                # 到達しない場合はNo
        print("No")


if __name__ == '__main__':
    Main()
