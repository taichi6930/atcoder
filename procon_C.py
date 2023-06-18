def main():
    k, a, b = map(int,  input().split())
    if b <= a:
        print(2 ** (k - 1))
        return
    print((b-a) * (k // 2) * (k % 2 + 1) - 1)


if __name__ == '__main__':
    main()
