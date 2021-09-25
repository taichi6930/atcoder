def main():
    s = list(input())
    a = []
    cnt = 0
    for i in range(10 ** 10):
        if cnt >= len(s):
            break
        if s[cnt] == '(':
            a.append(cnt)
        if s[cnt] == ')':
            t = ''.join(s[a[-1] + 1:cnt])
            u = t + t[::-1]
            s = s[0:a[-1]] + [u] + s[cnt + 1:]
            cnt = a[-1] + 1
            a.pop()
            continue
        cnt += 1

    print(''.join(s))


if __name__ == '__main__':
    main()
