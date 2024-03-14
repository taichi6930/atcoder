n = int(input())
P = list(map(int, input().split()))
print(max(P) - P[0] + 1 if P[0] != max(P) or P.count(max(P)) > 1 else 0)
