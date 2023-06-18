def main():
    maxa, maxb, maxc = 0, 0, 0
    n = int(input())
    for i in range(n):
        a, b, c = sorted(list(map(int, input().split())))
        maxa = max(a, maxa)
        maxb = max(b, maxb)
        maxc = max(c, maxc)
    print(maxa * maxb * maxc)


if __name__ == '__main__':
    main()
