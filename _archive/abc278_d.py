from collections import defaultdict
n = int(input())
A = defaultdict()
for p, a in enumerate(list(map(int, input().split()))):
    A[p + 1] = a
base_num = 0
q_num = int(input())
query_list = [list(map(int, input().split())) for _ in range(q_num)]

for query in query_list:
    q = query[0]
    if q == 1:
        x = query[1]
        base_num = x
        A = defaultdict()
        continue
    if q == 2:
        i = query[1]
        x = query[2]
        if not i in A:
            A[i] = base_num
        A[i] = x + A[i]
        continue
    if q == 3:
        i = query[1]
        if not i in A:
            print(base_num)
            continue
        print(A[i])
        continue
