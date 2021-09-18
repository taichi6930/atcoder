import math


def main():
    n = int(input())
    A = list(map(int,  input().split()))
    sumA = 0
    money = 1000
    for i in range(n - 1):
        if A[i + 1] - A[i] > 0:
            money += (A[i + 1] - A[i]) * math.floor(money / A[i])
    print(money)


if __name__ == '__main__':
    main()
