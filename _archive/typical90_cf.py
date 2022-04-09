from bisect import bisect_right
n = int(input())
s = list(input())

# oList = []
# xList = []

# for i in range(n):
#     if s[i] == 'o':
#         oList.append(i)
#         continue
#     xList.append(i)

# if len(oList) * len(xList) == 0:
#     print(0)
#     exit()

# lenXList = len(xList)
# lenOList = len(oList)

# ans = 0
# for i in range(n):
#     if s[i] == 'o':
#         x = bisect_right(xList, i)
#         if lenXList == x:
#             continue
#         ans += n - xList[x]
#     if s[i] == 'x':
#         x = bisect_right(oList, i)
#         if lenOList == x:
#             continue
#         ans += n - oList[x]

# print(ans)

kList = []

swi = s[0]
cnt = 0

for i in range(n):
    if swi == s[i]:
        cnt += 1
        continue
    kList.append(cnt)
    swi = s[i]
    cnt = 1
kList.append(cnt)

ans = n * (n + 1) // 2

for k in kList:
    ans -= k * (k + 1) // 2

print(ans)
