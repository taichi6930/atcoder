n, t = map(int, input().split())

listN = [list(map(int, input().split())) for _ in range(n)]

sumTime = 0
# for i in range(n):
#     sumTime = 0
#     listAB = list(map(int, input().split()))
#     a = listAB[0]
#     b = listAB[1]
# for j in range(n):
#     if listN[j] == 0:
#         listN[j] = listAB
#         break
#     else:
#         after = a * (sumTime + 1) + b
#         before = listN[j][0] * (sumTime + 1) + listN[j][1]
#         if before > after:

#         elif before < after:

print(listN)
