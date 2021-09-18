def main():
    n = int(input()) % 40

    print(1 if n == 0 else n if n <= 20 else 41 - n)


if __name__ == '__main__':
    main()
