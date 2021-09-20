from pprint import pprint
import collections
import sys
h, w = map(int, input().split())
c = [list(input()) for i in range(h)]
cnt = c.count('#')
d = None
e = collections.deque()


def dfs(x, y):
    print(d)
    if not(0 <= x < h) or not(0 <= y < w) or d[x][y] == ".":
        # 壁に当たるか、探索範囲外になった時は処理を終わらせる
        return

    if d[x][y] == "g" and len(e) == cnt - 1:
        # ゴールに到達した時はYesを出力して終了
        print(e)
        sys.exit()

    d[x][y] = "."  # 同じ場所を探索しないように#を入れる
    e.append([x, y])
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)


def main():
    # スタート位置を決める
    sx, sy = -1, -1
    for i in range(h):
        for j in range(w):
            d = c
            e = collections.deque()
            if d[i][j] == ".":
                continue
            d[i][j] = "s"
            e.append([i, j])
            if d[i][j] == "s":
                sx, sy = i, j
                break
        if sx + sy >= 0:
            break

    for i in range(h):
        for j in range(w):
            if d[i][j] == "." or d[i][j] == "s":
                continue
            d[i][j] = "g"
            if d[i][j] == "g":
                gx, gy = i, j
                break
        if gx + gy >= 0:
            break
    pprint(d)
    dfs(sx, sy)
    # 到達しない場合はNo
    print("No")


if __name__ == '__main__':
    main()
