def main():
    n = int(input())
    s = input()
    t = ''

    for i in range(n):
        u = s[-1]
        t += u
        s = s.replace(u, '')
        if len(s) <= 0:
            break
    print(t[::-1])


if __name__ == '__main__':
    main()
