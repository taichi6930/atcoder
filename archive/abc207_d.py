def main():
    n = int(input())
    abList, cdList = [None] * n, [None] * n
    for ab in range(n):
        abList[ab] = map(int, input().split())

    for cd in range(n):
        cdList[cd] = map(int, input().split())


if __name__ == '__main__':
    main()
