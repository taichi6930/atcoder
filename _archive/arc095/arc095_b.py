n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

ans1 = max(A)
mink = 0
k = max(A)

for a in A[1:]:
    if ans1 < abs(k / 2 - a):
        continue
    mink = a
    ans1 = abs(k / 2 - a)

print(k, mink)
