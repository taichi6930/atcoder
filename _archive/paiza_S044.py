from collections import defaultdict
from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))

a_dic = defaultdict()
a_dic[n] = set()
num_dic = defaultdict(list)

for i in range(n - 1,  -1, -1):
    setA_a = a_dic[i + 1].copy()
    setA_a.add(A[i])
    a_dic[i] = setA_a
    setA = setA_a

for i in range(n):
    num_dic[A[i]].append(i)

dic = defaultdict(None)

for i in range(n):
    if i == 0:
        for j in range(n - 1,  -1, -1):
            dic[str(A[j])] = j
    if i > 0:
        dic_old = dic.copy()
        dic = defaultdict()
        for key, value in dic_old.items():
            if value == n - 1:
                continue
            for k in list(a_dic[value + 1]):
                new_key = key + '_' + str(k)
                b = bisect_left(num_dic[k], value + 1)
                dic[new_key] = num_dic[k][b]
    print(len(dic))
