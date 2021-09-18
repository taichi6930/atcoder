def main():
    s, t = map(str, input().split())
    if 'B' in s:
        s = - int(s[1]) + 1
    else:
        s = int(s[0])
    if 'B' in t:
        t = - int(t[1]) + 1
    else:
        t = int(t[0])
    print(abs(s - t))


if __name__ == '__main__':
    main()
