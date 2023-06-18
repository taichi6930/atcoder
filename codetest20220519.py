T = int(input())
P = list(map(float, input().split()))
G = int(input())

S, E = 1, 1

ans = 0

for i in range(T):
    for j in range(i, T):
        nowans = sum(P[i: j + 1]) - G * (j - i + 1)
        if ans < nowans:
            ans = nowans
            S = i + 1
            E = j + 1

print(S, E)
