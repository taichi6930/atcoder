n = int(input())
H = list(map(int, input().split()))
t = 0

for h in H:
    t += h // 5 * 3
    h -= h // 5 * 5
    for _ in range(4):
        if h <= 0:
            break
        t += 1
        h += -3 if t % 3 == 0 else -1

print(t)
