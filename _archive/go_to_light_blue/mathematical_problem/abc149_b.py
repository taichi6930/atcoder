def main():
    a, b, k = map(int, input().split())
    print(max(a - k, 0), max(0, b - max(0, k - a)))


if __name__ == '__main__':
    main()
