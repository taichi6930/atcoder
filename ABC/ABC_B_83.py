# n, a, b = map(int, input().split())
# nSum = 0
# for i in range(n):
#     if a <= sum([int(d) for d in list(str(i + 1))]) <= b:
#         nSum += i + 1
# print(nSum)

n, a, b = map(int, input().split())
print(sum(i + 1 for i in range(0, n) if a <=
          sum([int(d) for d in list(str(i + 1))]) <= b))
