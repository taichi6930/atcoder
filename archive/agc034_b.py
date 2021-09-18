def main():
    s = list(input())
    n = len(s)

    ans = 0
    if n < 3:
        print(ans)
        return

    num = 0
    for i in range(10 ** 9):
        if num > n - 3:
            break
        if "".join(s[num: num + 3]) != "ABC":
            num += 1
            continue
        s[num] = "B"
        s[num + 1] = "C"
        s[num + 2] = "A"
        ans += 1
        num = max(0, num - 2)
    print(ans)


if __name__ == '__main__':
    main()
