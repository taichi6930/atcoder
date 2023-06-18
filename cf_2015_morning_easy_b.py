def main():
    n = int(input())
    s = list(input())
    ans = 0

    if n % 2 != 0:
        print(-1)
        return
    a = s[0: n // 2]
    b = s[n // 2: n]
    for i in range(n // 2):
        if a[i] != b[i]:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
