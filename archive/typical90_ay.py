import collections


class Main():

    def __init__(self):
        self.n, self.k, self.p = map(int, input().split())

        self.A = sorted(list(map(int, input().split())), reverse=True)
        print(self.n)

        self.main()
        self.display()

    def main(self):
        # d内が全て探索されているかどうかでループを続けるか判定
        while 0 in self.d:
            # まだ探索されていない頂点を探す
            i = self.d.index(0)
            # タイムスタンプ
            self.t = self.dfs(i + 1, self.t + 1)

    def dfs(self, x, t):
        # 探索済のチェックを行う（タイムスタンプ）
        self.d[x - 1] = t

        # 隣接リストを全て探索する
        for y in self.g[x - 1]:
            # 既に探索済ならスキップ
            if self.d[y - 1] > 0:
                continue
            t = self.dfs(y, t + 1)

        # 全て見終わったらfに入力する
        self.f[x - 1] = t + 1
        return t + 1

    def display(self):
        for i in range(self.n):
            print(i + 1, self.d[i], self.f[i])


if __name__ == '__main__':
    Main()
