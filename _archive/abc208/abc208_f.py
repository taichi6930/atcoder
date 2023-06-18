mod = 10 ** 9 + 7


def main():
    n, m, k = map(int, input().split())
    if n == 0:
        print(0)
        return
    if m == 0:
        a = 1
        for _ in range(k):
            b = n % mod
            a = (a * b) % mod
        print(a)
        return


if __name__ == '__main__':
    main()
