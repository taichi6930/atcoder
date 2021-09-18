def main():
    x, y = map(int, input().split())
    k = int(input())

    print(x + min(k, y) - max(0, k - y))


if __name__ == '__main__':
    main()
