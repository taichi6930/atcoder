mod = 10 ** 9 + 7


def main():
    n, k = map(int, input().split())
    ans = 1

    for i in range(k, n + 1):
        ans = (ans + (n - i + 1) * i + 1) % mod

    print(ans)


if __name__ == '__main__':
    main()
