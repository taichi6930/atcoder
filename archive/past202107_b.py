def main():
    a, b, c = map(int, input().split())
    print((a - max(a - b * c, 0)) / b)


if __name__ == '__main__':
    main()
