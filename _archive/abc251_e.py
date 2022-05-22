n = int(input())
A = list(input())

# A1を払う場合 -> 動物Nはまだ餌を食べていない
K1 = [A[0], A[0]] + [0 for _ in range(n)]
