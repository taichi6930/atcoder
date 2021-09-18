from itertools import accumulate


def main():
    n = int(input())
    A = sorted(list(map(int, input().split())))
    B = list(accumulate(A))
    print(B)


if __name__ == '__main__':
    main()
