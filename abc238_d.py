import math


def main():
    t = int(input())

    for i in range(t):
        a, s = map(int, input().split())
        x = a
        y = s - x

        if y < x:
            print('No')
            continue

        y2 = (y % (2 ** (math.ceil((math.log(a, 2))) + 1))) & a
        print('Yes' if x == y2 else 'No')


if __name__ == '__main__':
    main()
