# from collections import Counter
# n = int(input())
# A = sorted(list(map(int, input().split())))
# cA = Counter(A)

# lis = {}
# aMax = A[-1]

# cAkeys = sorted(list(cA.keys()))

# for i in range(len(cAkeys)):
#     for j in range(i, len(cAkeys)):
#         akp = cAkeys[i] * cAkeys[j]
#         if akp > aMax:
#             break
#         if not akp in lis:
#             lis[akp] = 0
#         lis[akp] += cA[cAkeys[i]] * cA[cAkeys[j]] * (1 if i == j else 2)

# lisans = list(set(lis.keys()) & set(A))
# print(sum([lis[ans] * cA[ans] for ans in lisans]))

from collections import Counter as ct

n = int(input())
a = list(map(int, input().split()))
a.sort()
b = list(set(a))
b.sort()
c = ct(a)

ans = 0
r = len(b)
for i, j in enumerate(b):
    for k, l in enumerate(b[i:]):
        if j * l >= b[-1]:
            break
        if not j * l in c:
            dic[j * l] = 0
        if j == l:
            dic[j * l] += c[j] * c[l]
        else:
            dic[j * l] += c[j] * c[l] * 2
print(dic)
