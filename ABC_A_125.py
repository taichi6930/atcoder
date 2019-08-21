#入力部分を取得
#A, B, C = map(int,input().split())

#sumを取得
#sum([A,B,C])

#importするとき
#import math

#配列に入れる
#b_list=list(map(int,input().split()))

#一つ代入する(数値)
#e=int(input())

#取得する
#e=input()

#切り捨て
#math.floor((3*A + P)/2)

import math

A, B, T = map(int,input().split())
print((math.floor((T+0.5)/A))*B)
