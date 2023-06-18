import math


def main():
    ans = 0
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ans = max(ans, (A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2)
    print(math.sqrt(ans))


if __name__ == '__main__':
    main()
