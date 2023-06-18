def main():
    n, a, b = map(int,  input().split())
    if n == 1:
        print(1 if a == b else 0)
        return
    if a > b:
        print(0)
        return

    print(1 + (b * (n - 1) + a) - (a * (n - 1) + b))


if __name__ == '__main__':
    main()
