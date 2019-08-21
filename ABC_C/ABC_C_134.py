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


N = int(input())
A_list = list(range(0))

top1Num = 0
top2Num = 0
topCount = 0

# countが必要

for i in range(N):
    A = int(input())
    A_list.append(A)
    if A > top1Num:
        top2Num = top1Num
        top1Num = A
    elif A > top2Num:
        top2Num = A

# print(A_list)
# print(top1Num)
# print(top2Num)

topCount = A_list.count(top1Num)
# print(topCount)

print("--------------------")

for i in range(N):
    if A_list[i] == top1Num:
        print(top2Num)
    else:
        print(top1Num)
