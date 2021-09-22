def main():
    n = int(input())
    C = list(map(int, input().split()))

    q = int(input())

    ans = 0

    for i in range(q):
        s = list(map(int, input().split()))

        if s[0] == 1:
            x = s[1]
            a = s[2]
            if C[x - 1] < a:
                continue
            ans += a
            C[x - 1] -= a
            continue

        a = s[1]

        if s[0] == 2:
            if min(C[0::2]) < a:
                continue
            ans += a * (int(n + 1) // 2)
            for i in range(int(n + 1) // 2):
                C[2 * i] -= a
            continue

        if s[0] == 3:
            if min(C) < a:
                continue
            ans += a * n
            C = list(map(lambda x: x - a, C))
            continue
    print(ans)


if __name__ == '__main__':
    main()
