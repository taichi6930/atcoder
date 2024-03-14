def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


n = int(input())
strN = str(n)
ans = None


def k(cnt, a):
    global ans
    if int(a) == 0:
        if ans is None:
            ans = cnt
            return
        ans = min(cnt, ans)
        return
    # ちゃんと払う
    # print(a, a[0] + "0" * (len(a) - 1))
    if len(a) == 1:
        k(cnt + int(a[0]), 0)
        k(cnt + 1 + (10 - int(a[0])), 0)
        return
    k(cnt + int(a[0]), a[1:])
    print(
        cnt + int(str(int(a[0]) + 1).replace("10", "1")),
        int(a) - int(str(int(a[0]) + 1) + "0" * (len(a) - 1)),
    )
    k(cnt + int(a[0]) + 1, a[1:])
    # print(a, str(int(a[0]) + 1) + "0" * (len(a) - 1))


k(0, strN)

print(ans)
