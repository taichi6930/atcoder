h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
# A には高さh, 幅wの行列が入っている
# Aの数字は全て異なる
# B には、Aの各々の要素と、その右、下にある要素が一緒に入るリストが入る
B = []
for i in range(h):
    for j in range(w):
        if j != w - 1:
            B.append(sorted([A[i][j], A[i][j + 1]]))
        if i != h - 1:
            B.append(sorted([A[i][j], A[i + 1][j]]))
# Bの要素を 1 2 のようにprintする
for b in sorted(B):
    print(*b)
