def main():
    a, b, c, d = map(int, input().split())
    print(min(d, a + b - c))


if __name__ == '__main__':
    main()
