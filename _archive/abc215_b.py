import math


def main():
    n = int(input())
    cnt = 0
    k = 1
    for i in range(100):
        if k * 2 > n:
            print(i)
            return
        k *= 2


if __name__ == '__main__':
    main()
