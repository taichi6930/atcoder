def main():
    n = int(input())
    s = input()
    cnt = s.count("R") * s.count("G") * s.count("B")

    for i in range(n - 2):
        for k in range(1, n):
            if i + 2 * k >= n:
                break
            if (s[i] != s[i + k]) and (s[i + k] != s[i + 2 * k]) and (s[i] != s[i + 2 * k]):
                cnt -= 1
    print(cnt)


if __name__ == '__main__':
    main()
