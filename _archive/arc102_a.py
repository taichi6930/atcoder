def main():
    n, k = map(int, input().split())
    ans = 0

    for i in range(k):
        ans += ((n + i) // k) ** 3
    print(ans)


if __name__ == '__main__':
    main()
