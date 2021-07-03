a, b, c, d = map(int, input().split())
k = b/a - d/c
if k > 0:
    print("TAKAHASHI")
elif k < 0:
    print("AOKI")
else:
    print("DRAW")
