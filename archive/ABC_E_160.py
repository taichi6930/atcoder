import math


def main():
    x, y, a, b, c = map(int, input().split())
    p = sorted(list(map(int, input().split())), reverse=True)[0:x]
    q = sorted(list(map(int, input().split())), reverse=True)[0:y]
    r = sorted(list(map(int, input().split())), reverse=True)
    pqr = sorted((p + q + r), reverse=True)
    print(sum(pqr[0:(x + y)]))


if __name__ == '__main__':
    main()
