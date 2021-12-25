from bisect import bisect_left


def main():
    n = int(input())
    S = list(input())
    oxList = ["o", "x"]
    ans = 0

    for i in range(n - 1):
        T = S[i + 1:]
        lenT = len(T)
        index = lenT

        if S[i] == 'o':
            index = bisect_left(T, 'x')
            if 'x' == T[0]:
                index = 0
            elif index == lenT:
                continue
            ans += lenT - index

        elif S[i] == 'x':
            index = bisect_left(T, 'o')
            if 'o' == T[0]:
                index = 0
            elif index == lenT:
                continue
            ans += lenT - index

    print(ans)


if __name__ == '__main__':
    main()
