n = int(input())
A = int(''.join(list(map(str, input().split()))), 2)


def calc(num, a):
    if a == 0:
        print('Yes')
        exit()
    if num == 0 and a == 1:
        return

    if a & 1 == 0:
        b = a >> 1
        calc(num - 1, b)
    if (a >> (num - 1)) & 1 == 0:
        b = a ^ (2 ** (num - 1) - 1)
        calc(num - 1, b)


calc(n, A)

print('No')
