def main():
    x, y, z = map(int, input().split())
    a = int(y * z / x)
    if a * x == y * z:
        a -= 1
    print(a)


if __name__ == '__main__':
    main()
