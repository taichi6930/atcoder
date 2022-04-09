n = int(input())
A = int(''.join(list(map(str, input().split()))), 2)
binA = ''.join('{:0' + str(n) + 'b}').format(A)
ans = False


def calc(num, lis):
    global ans
    print(int(lis, 0)
    if num == 0:
        ans = True
        return
    # 末尾が0である場合、取り外す
    if lis & 1 == 0:
        lis = lis >> 1
        calc(num - 1, lis)

    # 末尾が0でない場合、先頭が0である場合、取り外してから、flipする


calc(n, binA)
