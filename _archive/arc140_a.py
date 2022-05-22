from collections import Counter, deque
n, k = map(int, input().split())
s = input()
ss = s + s[:-1]
print(ss)

sSet = set()

for i in range(n):
    sSet.add(ss[i: n + i])

print(sSet)
# cS = Counter(S)
# valueS = deque(sorted(cS.values()))

# for i in range(len(valueS) - 1):
#     num = min(valueS[0], k)
#     valueS[0] -= num
#     k -= num
#     if valueS[0] == 0:
#         valueS.popleft()

# print(len(valueS))
