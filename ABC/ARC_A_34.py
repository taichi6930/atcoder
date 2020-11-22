def main():
    n = int(input())
    maxK = 0
    for i in range(n):
        li = list(map(int, input().split()))
        maxK = max(maxK, sum(li) - li[-1] * 79 / 90)
    print(maxK)


if __name__ == '__main__':
    main()
