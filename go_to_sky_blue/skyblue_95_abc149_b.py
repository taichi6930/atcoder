def main():
    a, b, k = map(int, input().split())
    print(max(0, a - k), max(min(b - k + a, b), 0))


if __name__ == '__main__':
    main()
