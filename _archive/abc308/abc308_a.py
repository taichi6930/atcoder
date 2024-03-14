S = list(map(int, input().split()))
for i, s in enumerate(S):
    if s % 25 != 0 or 100 > s or s > 675:
        exit(print("No"))
print("Yes" if S == sorted(S) else "No")
