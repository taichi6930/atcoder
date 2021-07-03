def engJudge(x):
    engList = ["A", "B", "C", "D", "E"]
    cnt = 1
    for i in engList:
        if i == x:
            return cnt
        cnt += 1


print(engJudge(input()))
