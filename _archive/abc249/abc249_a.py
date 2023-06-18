a, b, c, d, e, f, x = map(int, input().split())

ta, ao = 0, 0
tax, aox = x, x

for i in range(100):
    if tax <= a + c:
        ta += min(tax, a) * b
        break
    ta += a * b
    tax -= (a + c)

for i in range(100):
    if aox <= d + f:
        ao += min(aox, d) * e
        break
    ao += d * e
    aox -= (d + f)

if ta > ao:
    print("Takahashi")
elif ao > ta:
    print("Aoki")
else:
    print("Draw")