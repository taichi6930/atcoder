n, d = map(int, input().split())
K = ["o" for _ in range(d)]
for s in [list(input()) for _ in range(n)]:
    for i in range(d):
        if s[i] == "x":
            K[i] = "x"
print(max(list(len(i) for i in "".join(K).split("x"))))
