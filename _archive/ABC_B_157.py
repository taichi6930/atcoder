a = []
for _ in range(3):
    a.extend(list(input().split()))

n = int(input())
for _ in range(n):
    k = input()
    for i in range(9):
        if a[i] == str(k):
            a[i] = 0

ans = False

if a[0] == a[1] and a[1] == a[2] and a[2] == 0:
    ans = True

if a[3] == a[4] and a[4] == a[5] and a[5] == 0:
    ans = True

if a[6] == a[7] and a[7] == a[8] and a[8] == 0:
    ans = True

if a[0] == a[3] and a[3] == a[6] and a[6] == 0:
    ans = True

if a[1] == a[4] and a[4] == a[7] and a[7] == 0:
    ans = True

if a[2] == a[5] and a[5] == a[8] and a[8] == 0:
    ans = True

if a[0] == a[4] and a[4] == a[8] and a[8] == 0:
    ans = True

if a[2] == a[4] and a[4] == a[6] and a[6] == 0:
    ans = True

print("Yes" if ans else "No")
