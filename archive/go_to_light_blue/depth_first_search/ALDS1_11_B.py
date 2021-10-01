def dfs(x, t):
    global g, d, f
    # 探索済のチェックを行う（タイムスタンプ）
    d[x - 1] = t

    # 隣接リストを全て探索する
    for y in g[x - 1]:
        # 既に探索済ならスキップ
        if d[y - 1] > 0:
            continue
        t = dfs(y, t + 1)

    # 全て見終わったらfに入力する
    f[x - 1] = t + 1
    return t + 1


# 頂点の数を作成
n = int(input())
# 隣接リストを作成
g = [list(map(int, input().split()))[2::] for _ in range(n)]

# 最初に発見した時刻を記録
d = [0] * n
# 完了時刻を記録
f = [0] * n

# ストップウォッチ
t = 0

# d内が全て探索されているかどうかでループを続けるか判定
while 0 in d:
    # まだ探索されていない頂点を探す
    i = d.index(0)
    # タイムスタンプ
    t = dfs(i + 1, t + 1)

for i in range(n):
    print(i + 1, d[i], f[i])
