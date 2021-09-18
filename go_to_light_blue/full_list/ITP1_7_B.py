def main():
    while True:
        ans = 0
        n, x = map(int, input().split())

        if (n, x) == (0, 0):
            return

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if i + j + k + 3 == x:
                        ans += 1
        print(ans)


if __name__ == '__main__':
    main()
