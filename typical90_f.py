def main():
    n, k = map(int, input().split())
    s = list(input())

    a = 0

    str = ""

    for i in range(k):
        s1 = s[a: n - k + i + 1]
        s1sorted = sorted(s1)
        str += s1sorted[0]
        a += s1.index(s1sorted[0]) + 1

    print(str)


if __name__ == '__main__':
    main()
