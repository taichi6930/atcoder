def main():
    s = list(input().replace('BC', 'D'))
    cnt, ans = 0, 0
    for _ in range(10 ** 10):
        if len(s) <= cnt + 1:
            break
        s1, s2 = s[cnt], s[cnt + 1]
        if s1 == 'A' and s2 == 'D':
            ans += 1
            s[cnt: cnt + 2] = ['D', 'A']
            cnt = max(cnt - 1, 0)
            continue
        cnt += 1
    print(ans)


if __name__ == '__main__':
    main()
