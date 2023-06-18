S = list(input())

for s in S:
    if S.count(s) == 1:
        exit(print(s))

print(-1)
