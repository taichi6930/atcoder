import time
import sys

# nを取得
n = int(input())

start = time.time()

a = [0, 0, 1]

# nが3以下の場合はa配列内の数値で出せる
if n <= 3:
    print(a[n - 1])
else:
    for i in range(3, n):

        # # トリボナッチ計算をする
        # aNew = a[0] + a[1] + a[2]

        # # 新しい配列を作る(10007の余り)
        # a[0] = a[1] % 10007
        # a[1] = a[2] % 10007
        # a[2] = aNew % 10007

        # 新しい配列を作る
        a[0], a[1], a[2] = a[1], a[2], (a[0] + a[1] + a[2]) % 10007

    print(a[2] % 10007)

finish = time.time()

print("time", finish-start)
