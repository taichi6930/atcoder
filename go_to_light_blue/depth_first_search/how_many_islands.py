w, h = map(int, input().split())
c = [list(map(int, input().split())).replace(1, -1) for _ in range(h)]
ans = 0
swi = 0


def dfs(x, y):
    if not(0 <= x < h) or not(0 <= y < w) or c[x][y] == 0:
        # 壁に当たるか、探索範囲外になった時は処理を終わらせる
        return

    if c[x][y] == 0:
        # ゴールに到達した時はYesを出力して終了
        return

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
