def main():
    n = int(input())
    A = list(map(int, input().split()))
    print(A.index(sorted(A, reverse=True)[1]) + 1)


if __name__ == '__main__':
    main()
