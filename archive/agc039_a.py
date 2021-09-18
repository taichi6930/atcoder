def main():
    s = list(input())
    k = int(input())
    ans = 0

    if len(s) == 1:
        print(len(s) // 2)
        return

    for l in range(len(s) - 1):
        if s[l] == s[l + 1]:
            ans += 1
            s[l + 1] = str(l)

    ans *= k

    print(ans + (0 if s[len(s) - 1] != s[0] else k - 1))


if __name__ == '__main__':
    main()
