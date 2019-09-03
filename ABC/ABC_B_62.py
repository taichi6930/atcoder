h, w = map(int, input().split())

a = "".join(["#"] * (w + 2))

print(a)
for i in range(h):
    print("#" + input() + "#")

print(a)
