n = int(input())
A = int(''.join(list(map(str, input().split()))), 2)
ans = False


def calc(num, a):
    print(num, a, ''.join('{:0' + str(num) + 'b}').format(a[-1]))
    global ans
    if ans:
        return
    if num == 0 and a[-1] == 0:
        ans = True
        return

    # 一番下が0であれば、シフト1回する
    if a[-1] & 1 == 0:
        b = a[-1] >> 1
        calc(num - 1, a + [b])
    if (a[-1] >> (num - 1)) & 1 == 0:
        b = a[-1] ^ (2 ** (num - 1) - 1)
        calc(num - 1, a + [b])


calc(n, [A])

print(ans)
