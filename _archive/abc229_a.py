def main():
    s = [list(input()) for _ in range(2)]
    ans = 'Yes'

    for i in range(2):
        for j in range(2):
            if s[i][j] == '#' and s[i][1 - j] == '.' and s[1 - i][j] == '.':
                ans = 'No'
    print(ans)


if __name__ == '__main__':
    main()
