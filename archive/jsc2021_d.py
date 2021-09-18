def main():
    mod = 10 ** 9 + 7
    n, p = map(int, input().split())
    print((p - 1) * pow(p - 2, n - 1, mod) % mod)


if __name__ == '__main__':
    main()
