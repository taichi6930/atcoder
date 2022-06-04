a, b, c = map(int, input().split())

P = [1]

for i in range(100):
    d = (P[-1] * a) % 10
    if d in P[1:]:
        continue
    P.append(d)
P[0] = P[-1]

e = pow(b, c, max(1, len(P) - 1))

print(P[e])
