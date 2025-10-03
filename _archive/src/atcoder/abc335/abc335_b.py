n = int(input())
for a in range(n + 1):
    for b in range(n + 1 - a):
        for c in range(n + 1 - a - b):
            print(a, b, c)