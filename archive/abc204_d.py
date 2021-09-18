import math


def main():
    n = int(input())
    T = sorted(list(map(int, input().split())), reverse=True)

    maxMinT = math.ceil(sum(T) / 2)
    a = 0

    for i in range(n):
        if a + T[i] > maxMinT:
            continue
        a += T[i]

    print(max(sum(T) - a, a))


if __name__ == '__main__':
    main()
