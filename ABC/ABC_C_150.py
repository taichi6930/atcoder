# # nの定義
# n = int(input())

# # p,qの定義
# p, q = [list(map(int, input().split())) for _ in range(2)]

# # 全体数,nListを定義
# sumN = 1
# pList = [0] * n
# qList = [0] * n
# for i in range(n):
#     sumN *= i + 1
#     pList[i] = i + 1
#     qList[i] = i + 1

# sumN = sumN // n

# pSum = 0
# qSum = 0

# for i in range(n - 1):
#     pSum += pList.index(p[i]) * sumN
#     pList.pop(pList.index(p[i]))

#     qSum += qList.index(q[i]) * sumN
#     qList.pop(qList.index(q[i]))

#     sumN = sumN // (n - i - 1)

# print(abs(pSum - qSum))
import itertools

n = int(input())
p, q = [tuple(map(int, input().split())) for _ in range(2)]

nList = list(itertools.permutations([i for i in range(1, n+1)]))

print(abs(nList.index(p) - nList.index(q)))
