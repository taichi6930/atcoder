def main():
    n = int(input())

    ans = ""

    for i in range(120):
        if n % 2 == 0:
            ans += "B"
            n = n // 2
            continue
        ans += "A"
        n -= 1

        if n == 0:
            break

    print(ans[::-1])


if __name__ == '__main__':
    main()
