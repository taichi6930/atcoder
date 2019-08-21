# 入力部分を取得
# A, B, C = map(int,input().split())

# sumを取得
# sum([A,B,C])

# importするとき
# import math

# 配列に入れる
# b_list=list(map(int,input().split()))

# 一つ代入する(数値)
# e=int(input())

# 取得する
# e=input()

# 切り捨て
# math.floor((3*A + P)/2)

# stringからdatetimeへ変換
# 例1
# string_date_1 = '2017/07/01'
# atetime.datetime.strptime(string_date_1, '%Y/%m/%d')

# forの使い方
# for i in range(3):
#    print(haiku[i])
# for haiku in haikus:
#    print(haiku)

# 分割して受け取る
# haiku = haikus.split(",")

# 文字列の分割
# char_list = list(str)

# ソートする
# n = int(input())
# d = list(map(int, input().split()))
# list = sorted(d)
# print(d)

# 文字列の連結
# A = join(str)

import math

cnt = 0

N, D = map(int, input().split())
X = []
for l in range(N):
    X.append(list(map(int, input().strip().split())))

for i in range(0, N - 1):
    for j in range(i + 1, N):
        sum = 0
        for k in range(0, D):
            sum += (X[i][k] - X[j][k])**2
        if math.sqrt(sum) == int(math.sqrt(sum)):
            cnt += 1
print(cnt)
