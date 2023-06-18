import math


def main():
    a, b, n = map(int,  input().split())
    maxt = 0
    for x in range(n):
        maxt = max(maxt, math.floor(a * (x + 1) / b) -
                   a * math.floor((x+1) / b))
    print(maxt)


if __name__ == '__main__':
    main()
