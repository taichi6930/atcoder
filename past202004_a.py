
def main():
    s, t = map(str, input().split())

    s = int(s[0]) if 'F' in list(s) else -int(s[1]) + 1
    t = int(t[0]) if 'F' in list(t) else -int(t[1]) + 1

    print(abs(s - t))


if __name__ == '__main__':
    main()
