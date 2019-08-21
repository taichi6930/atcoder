#入力部分を取得
#A, B, C = map(int,input().split())

#sumを取得
#sum([A,B,C])

A, B= map(int,input().split())
if A>=13:
    print(B)
elif 6<=A:
     print(int(B/2))   
else:
    print(0)
