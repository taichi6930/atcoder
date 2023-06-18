def main():
    n = int(input())
    A = list(map(int, input().split()))

    print((A[-1] - A[0]) / (n - 1))


if __name__ == '__main__':
    main()
