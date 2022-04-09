def main():
    x1, y1, x2, y2 = map(int, input().split())
    l = (x2 - x1) ** 2 + (y2 - y1) ** 2

    if l > 20:
        print('No')
        return

    for a in range(min(x1, x2) - 10, max(x1, x2) + 10):
        for b in range(min(y1, y2) - 10, max(y1, y2) + 10):
            p = (a - x1) ** 2 + (b - y1) ** 2
            q = (a - x2) ** 2 + (b - y2) ** 2

            if p == 5 and q == 5:
                print('Yes')
                return

    print('No')


if __name__ == '__main__':
    main()
