t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    swi = True
    for i in range(1, n):
        a, b = s[:i], s[i:]
        if "".join([a, b]) == "".join(sorted([a, b])):
            swi = False
    print("No" if swi else "Yes")
