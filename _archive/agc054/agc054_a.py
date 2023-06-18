import math


def main():
    n = int(input())
    S = list(input())

    if S[0] != S[-1]:
        print(1)
        return
    if len(S) <= 3:
        print(-1)
        return
    st = S[1: -1]
    k = S[0]
    for i in range(len(st) - 1):
        if st[i] != k and st[i + 1] != k:
            print(2)
            return
    print(-1)


if __name__ == '__main__':
    main()
