T = int(input())

for t in range(T):
    n, a, b, x, y, z = map(int, input().split())
    y = min(y, a * x)
    z = min(z, b * x)
    score = 0

    # ABで最小なものを引いておく
    score += (n // (a * b)) * min(a * b * x, b * y, a * z)
    n -= (n // (a * b)) * a * b

    # xのみ使用
    ans = n * x
    n1 = n * 1
    n2 = n * 1
    n3 = n * 1
    n4 = n * 1

    # yを目一杯使い、zを目一杯使い、あまりをx使用
    ans1 = y * (n1 // a)
    n1 -= (n1 // a) * a
    ans1 += z * (n1 // b)
    n1 -= (n1 // b) * b
    ans1 += x * n1

    # yを目一杯使い、あまりをx使用
    ans2 = y * (n2 // a) + x * (n2 - (n2 // a) * a)

    # yを目一杯使い、zを目一杯使い、あまりをx使用
    ans3 = z * (n3 // b)
    n3 -= (n3 // b) * b
    ans3 += y * (n3 // a)
    n3 -= (n3 // a) * a
    ans3 += x * n3

    # zを目一杯使い、あまりをx使用
    ans4 = z * (n4 // b) + x * (n4 - (n4 // b) * b)

    print(score + min(ans, ans1, ans2, ans3, ans4))
