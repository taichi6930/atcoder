def main():
    l, r = map(int, input().split())
    s = input()
    print(s[0: l - 1] + s[l - 1: r][::-1] + s[r:])


if __name__ == '__main__':
    main()
