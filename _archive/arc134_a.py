from math import ceil
n, l, w = map(int, input().split())
A = [-w] + list(map(int, input().split())) + [l]

ans = 0

for i in range(len(A) - 1):
    # print(A[i], A[i + 1], max(0, A[i + 1] - (A[i] + w)))
    ans += ceil(max(0, A[i + 1] - (A[i] + w - 1)) / w)
print(ans)
# coverList = [[0, 0]]
# coverl = []
# for i, a in enumerate(A):
#     if len(coverl) == 0:
#         coverl.append(a)
#         continue
#     if a - coverl[-1] > w:
#         coverl.append(coverl[-1] + w)
#         coverList.append([coverl[0], coverl[-1]])
#         coverl = [a]
#     coverl.append(a)

# coverl.append(min(l, coverl[-1] + w))
# coverList.append([coverl[0], coverl[-1]])
# coverList.append([l, l])
# coverl = []

# ans = 0
# for i in range(len(coverList) - 1):
#     ans += ceil((coverList[i + 1][0] - coverList[i][-1]) / w)

# print(ans)
