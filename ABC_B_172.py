def main():
    s = input()
    t = input()
    cnt = 0
    for k in range(len(s)):
        cnt += 1 if s[k] != t[k] else 0
    print(cnt)


if __name__ == '__main__':
    main()
