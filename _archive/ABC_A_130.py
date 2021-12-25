#入力部分を取得
#A, B, C = map(int,input().split())

#sumを取得
#sum([A,B,C])

A, B, C = map(int,input().split())
print(sum([A,B,C])-max(A,B,C))