import math


def main():
    n = int(input())

    for i in range(50001):
        k = math.floor(i * 1.08)
        if n == k:
            print(i)
            return
    print(':(')


if __name__ == '__main__':
    main()
