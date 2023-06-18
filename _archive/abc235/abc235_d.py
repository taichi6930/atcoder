
ans = 10 ** 10
swi = False
a, n = map(int, input().split())


def q(x, cnt, lis):
    global ans, swi
    if x == 1:

        ans = min(cnt, ans)
        swi = True
        return

    if cnt > ans:
        return

    if x in lis:
        return
    lis.append(x)

    # 1つ目の方法
    if x % a == 0:
        y = x // a
        q(y, cnt + 1, lis)

    # 2つ目の方法
    strX = str(x)
    if len(strX) == 1:
        return
    z = strX[1:] + strX[0]
    q(int(z), cnt + 1, lis)


q(n, 0, [])
print(ans if swi else -1)
