w, h = set(), set()
for i in range(10):
    S = list(input())
    for j, s in enumerate(S):
        if s == '#':
            w.add(i + 1)
            h.add(j + 1)

print(min(w), max(w))
print(min(h), max(h))
