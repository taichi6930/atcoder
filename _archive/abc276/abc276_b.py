def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


n, m = map(int, input().split())
AB = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    AB[a - 1].append(b)
    AB[b - 1].append(a)

for ab in AB:
    if len(ab) == 0:
        print(0)
        continue
    print(' '.join([str(len(ab)), ' '.join(int2strWithArray(sorted(ab)))]))
