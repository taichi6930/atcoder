def main():
    s = list(input())
    t = list(input())
    ans = 'No'
    if s == t:
        ans = 'Yes'
    for i in range(len(s) - 1):
        u = ''.join(s[:i] + [s[i + 1]] + [s[i]] + s[i + 2:])
        if u == ''.join(t):
            ans = 'Yes'
            break
    print(ans)


if __name__ == '__main__':
    main()
