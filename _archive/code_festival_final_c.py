def main():
    a = int(input())

    for i in range(10, 10 ** 5 + 1):
        strI = list(str(i))

        sumI = 0

        for j in range(len(strI)):
            sumI += int(strI[j]) * (i ** (len(strI) - j - 1))

        if sumI == a:
            print(i)
            return
    print(-1)


if __name__ == '__main__':
    main()
