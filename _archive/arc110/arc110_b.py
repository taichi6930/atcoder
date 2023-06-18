def main():
    n = int(input())
    t = input()

    s = '110' * ((n + 9) // 3)
    k = s.find(t)
    if k < 0:
        print(0)
        return

    if n >= 2:
        print((3 * 10 ** 10 - (n + k)) // 3 + 1)
        return
    if n == 1:
        print(10 ** 10 * (int(t) + 1))
        return


if __name__ == '__main__':
    main()
