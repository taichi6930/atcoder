def main():
    s = list(input())
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            print("NO")
            return

    print("YES")


if __name__ == '__main__':
    main()
