def main():
    n, c, k = map(int, input().split())
    T = sorted([int(input()) for _ in range(n)])
    print(T)
    cnt = 0
    now = 0

    while cnt <= n:
        arr = T[cnt:min(len(T), c + cnt)]


if __name__ == '__main__':
    main()
