def main():
    for _ in range(10 ** 10):
        n, x = map(int, input().split())

        if n == 0 and x == 0:
            return

        ans = 0
        for i in range(1, n):
            if x < i:
                break
            for j in range(i + 1, n + 1):
                if x < (i + j):
                    break
                k = x - i - j
                if j >= k:
                    break
                if k <= n:
                    ans += 1
        print(ans)


if __name__ == '__main__':
    main()
