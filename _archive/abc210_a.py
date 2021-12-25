def main():
    n, a, x, y = map(int, input().split())

    print(x * n + max(0, n - a) * (y - x))


if __name__ == '__main__':
    main()
