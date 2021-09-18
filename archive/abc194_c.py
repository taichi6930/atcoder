import math


def main():
    n = int(input())
    A = list(map(int, input().split()))
    A2 = [A[i] ** 2 for i in range(n)]
    print(n * sum(A2) - sum(A) ** 2)


if __name__ == '__main__':
    main()
