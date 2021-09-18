alphaList = list("abcdefghijklmnopqrstuvwxyz")


def main():
    P = list(map(int, input().split()))
    Q = [alphaList[P[i] - 1] for i in range(26)]
    print(''.join(Q))


if __name__ == '__main__':
    main()
