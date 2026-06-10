n, k, m = map(int, input().split())
# cは色、vは価値
cv = {}
for _ in range(n):
    c, v = map(int, input().split())
    if c not in cv:
        cv[c] = []
    cv[c].append(v)

# 色ごとに一番高いものだけの配列を作成
max_cv = []
for c in cv:
    max_cv.append(max(cv[c]))

# 全体の価値の配列を作成
all_cv = []
for c in cv:
    for v in cv[c]:
        all_cv.append(v)

ans = 0

# 最初にmax_cvを降順にソートして、上からm個の価値を足す
max_cv.sort(reverse=True)
ans = sum(max_cv[:m])

# max_cvで使った数字をall_cvから削除する
for i in range(m):
    all_cv.remove(max_cv[i])

# all_cvを降順にソートして、上からk-m個の価値を足す
all_cv.sort(reverse=True)
ans += sum(all_cv[: k - m])

print(ans)
