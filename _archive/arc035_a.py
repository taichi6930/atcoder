def main():
    s = list(input())
    n = len(s)
    for i in range(n // 2):
        if s[i] != "*" and s[n - i - 1] != "*" and s[i] != s[n - i - 1]:
            print("NO")
            return
    print("YES")


if __name__ == '__main__':
    main()
