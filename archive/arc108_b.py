def main():
    n = int(input())
    S = list(input())
    T = ""

    ans = 0
    num = 0

    for s in S:
        T += s
        if T[max(0, len(T) - 3):] == 'fox':
            T = T[:len(T) - 3]
    print(len(T))


if __name__ == '__main__':
    main()
