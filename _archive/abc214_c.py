n = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

for i in range(2 * n):
    T[(i + 1) % n] = min(T[i % n] + S[i % n], T[(i + 1) % n])

for i in range(n):
    print(T[i])
