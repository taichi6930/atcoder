from pprint import pprint
h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
B = [list(map(int, input().split())) for _ in range(h)]

ans = 0

for i in range(h):
    for j in range(w):
        if j == w - 1 or i == h - 1:
            if A[i][j] != B[i][j]:
                print('No')
                exit()
            continue
        k = A[i][j] - B[i][j]
        ans += abs(k)
        for p in range(0, 2):
            for q in range(0, 2):
                B[i + p][j + q] += k

print('Yes')
print(ans)
