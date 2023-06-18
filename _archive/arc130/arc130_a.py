def main():
    n = int(input())
    S = list(input())
    ans = 0
    cnt = 0
    k = ""

    for i in range(n):
        s = S[i]
        if s == k:
            cnt += 1
        if s != k or i == n - 1:
            ans += cnt * (cnt + 1) // 2
            cnt = 0
        k = s
    print(ans)


if __name__ == '__main__':
    main()
