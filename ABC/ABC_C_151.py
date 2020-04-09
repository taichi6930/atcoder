# 問題数 = n と 回答数 = m を取得
n, m = map(int, input().split())

# 必要な変数を定義
ac = [0] * n
wa = [0] * n

for i in range(m):
    # i+1 回目の結果を取得
    p, s = list(input().split())
    p = int(p) - 1

    # ACではない場合
    if s == "WA" and ac[p] != 1:
        wa[p] = 1

    # ACである場合
    if s == "AC":
        ac[p] = 1

print(sum(ac), sum(wa))

