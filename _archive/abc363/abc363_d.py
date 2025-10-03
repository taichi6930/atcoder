n = int(input())
for i in range(1, 10):
    # i桁の時の数の合計
    k = 10 ** (i // 2 + 1) - 1
    print(f"{i}桁の時の数の合計: {k}")
