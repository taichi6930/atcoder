def main():
    N = input()
    s = 0
    l = [0 for i in range(3)]
    for n in N:
        n = int(n)
        l[n % 3] += 1
        s = (n + s) % 3
    if s == 0:
        print(0)
        return

    if l[s] > 0 and len(N) > 1:
        print(1)
        return

    if len(N) > 2:
        print(2)
        return

    print(-1)


if __name__ == '__main__':
    main()
