def main():
    n = int(input())
    sumA = 0
    for i in range(n):
        a, b = map(int, input().split())
        sumA += (a + b) * (b - a + 1) // 2
    print(sumA)


if __name__ == '__main__':
    main()
