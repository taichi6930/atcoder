def main():
    n, x = map(int, input().split())
    s = list(input())
    ans = 0
    ans += x

    for i in range(n):
        if s[i] == "o":
            ans += 1
            continue
        ans = max(0, ans - 1)
    print(ans)


if __name__ == '__main__':
    main()
