def main():
    n = int(input())
    for i in range(100):
        if n > 130000000:
            print(n)
            return
        n *= 2


if __name__ == '__main__':
    main()
