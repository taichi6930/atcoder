def main():
    n, m = map(int, input().split())

    for i in range(100):
        print(i + 1, ((10 ** (i + 1)) // m) % m)


if __name__ == '__main__':
    main()
