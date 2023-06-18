def main():
    n, a, b = map(int, input().split())
    aa, bb = 0, 0

    for i in range(10000):
        if n - a <= 0:
            aa += n
            n = 0
            print('Ant')
            break
        aa += a
        n -= a

        if n - b <= 0:
            bb += n
            n = 0
            print('Bug')
            break
        bb += b
        n -= b


if __name__ == '__main__':
    main()
