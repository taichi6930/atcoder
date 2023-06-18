def main():
    s = input()
    t = input()

    ans = -1

    for i in range(len(s)):
        ss = s[(-1 * i):] + s[0:(-1 * i)]
        if t == ss:
            ans = i
            break
    print(ans)


if __name__ == '__main__':
    main()
