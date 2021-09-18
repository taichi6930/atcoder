def main():
    n, m = map(int,  input().split())
    sumA = 0
    for i in range(m, n + 1):
        print((i + 1)/2 * i)


if __name__ == '__main__':
    main()
