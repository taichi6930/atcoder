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

A, B = list(map(int, input().split()))
if A == 1:
    if B == 1:
        print("Draw")
    else:
        print("Alice")
elif B == 1:
    print("Bob")
else:
    if A > B:
        print("Alice")
    elif A == B:
        print("Draw")
    else:
        print("Bob")
