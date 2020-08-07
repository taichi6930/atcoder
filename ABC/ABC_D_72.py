import math


def main():
    n = int(input())
    P = list(map(int, input().split()))
    cnt = 0
    for i in range(n - 1):
        if P[i + 1] == (i + 2):
            P[i + 1], P[i + 2] = (i + 2)
            cnt += 1
    print((cnt + 1)//2)


if __name__ == '__main__':
    main()
