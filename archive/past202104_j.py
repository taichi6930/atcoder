def main():
    n, c = map(int, input().split())
    x, x2, y, y2 = 0, 0, 0, 0

    for i in range(n):
        a, b = map(int, input().split())
        x += a
        x2 += a ** 2
        y += b
        y2 += b ** 2

    p = x / n

    ans = n * ((x / n) ** 2 + c ** 2) - 2 * ((x / n) * x + c * y) + (x2 + y2)
    print(ans)


if __name__ == '__main__':
    main()
