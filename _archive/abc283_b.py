n = int(input())
A = list(map(int, input().split()))
for q in range(int(input())):
    query = list(map(int, input().split()))
    if query[0] == 1:
        A[query[1] - 1] = query[2]
        continue
    if query[0] == 2:
        print(A[query[1] - 1])
        continue
