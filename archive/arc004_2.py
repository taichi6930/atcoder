def main():
    n = int(input())
    maxD = 0
    sumD = 0
    for i in range(n):
        d = int(input())
        maxD = max(d, maxD)
        sumD += d

    print(sumD)
    print(max(0, 2 * maxD - sumD))


if __name__ == '__main__':
    main()
