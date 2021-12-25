mod = 10 ** 9 + 7


def main():
    n = int(input())
    ans = 0
    for k in range(n + 1):
        maxNum = int(min(n, (n + k ** 2) ** 0.5))
        minNum = 1 + k
        ans2 = maxNum - minNum + 1
        if ans2 <= 0:
            break
        ans = (ans2 + ans) % mod
    print(ans)


if __name__ == '__main__':
    main()
