# 入力部分を取得
#A, B, C = map(int,input().split())

# sumを取得
# sum([A,B,C])

# importするとき
#import math

# 配列に入れる
# b_list=list(map(int,input().split()))

# 一つ代入する(数値)
# e=int(input())

# 取得する
# e=input()

# 切り捨て
#math.floor((3*A + P)/2)

# stringからdatetimeへ変換
# 例1
#string_date_1 = '2017/07/01'
#atetime.datetime.strptime(string_date_1, '%Y/%m/%d')

# forの使い方
# for i in range(3):
#    print(haiku[i])
# for haiku in haikus:
#    print(haiku)

# 分割して受け取る
#haiku = haikus.split(",")

# 文字列の分割
#char_list = list(str)

# ソートする
#n = int(input())
#d = list(map(int, input().split()))
#list = sorted(d)
# print(d)

import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True
