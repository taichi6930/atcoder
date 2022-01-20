# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B

def dfs(x, t):
    global graph, discoveryTime, finishTime
    # 探索済のチェックを行う（タイムスタンプ）
    discoveryTime[x - 1] = t

    # 隣接リストを全て探索する
    for y in graph[x - 1]:
        # 既に探索済ならスキップ
        if discoveryTime[y - 1] > 0:
            continue
        t = dfs(y, t + 1)

    # 全て見終わったらfに入力する
    finishTime[x - 1] = t + 1
    return t + 1


# 頂点の数を作成
n = int(input())
# 隣接リストを作成
graph = [list(map(int, input().split()))[2::] for _ in range(n)]

# 最初に発見した時刻を記録
discoveryTime = [0] * n
# 完了時刻を記録
finishTime = [0] * n

# ストップウォッチ
t = 0

# d内が全て探索されているかどうかでループを続けるか判定
while 0 in discoveryTime:
    # まだ探索されていない頂点を探す
    i = discoveryTime.index(0)
    # タイムスタンプ
    t = dfs(i + 1, t + 1)

for i in range(n):
    print(i + 1, discoveryTime[i], finishTime[i])
