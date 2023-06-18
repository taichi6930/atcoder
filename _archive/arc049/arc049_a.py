def main():
    s = input()
    A = sorted(list(map(int, input().split())), reverse=True)

    for a in A:
        s = s[:a] + '"' + s[a:]
    print(s)


if __name__ == '__main__':
    main()
