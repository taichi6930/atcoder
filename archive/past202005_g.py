# この問題 https://atcoder.jp/contests/atc001/tasks/dfs_a

# 値の入力
import sys
n, x, y = map(int, input().split())
h, w = y + 1, x + 1
c = [[None for _ in range(w)] for _ in range(h)]
ans = 10 ** 10


def dfs(x, y):
    if not(0 <= x < h) or not(0 <= y < w) or c[x][y] == "#":
        # 壁に当たるか、探索範囲外になった時は処理を終わらせる
        return

    if c[x][y] == "g":
        # ゴールに到達した時はYesを出力して終了
        print("Yes")
        sys.exit()

    c[x][y] = "#"  # 同じ場所を探索しないように#を入れる
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)


def main():
    # スタート位置を決める
    sx, sy = 0, 0
    dfs(sx, sy)
    # 到達しない場合はNo
    print("No")


if __name__ == '__main__':
    main()
