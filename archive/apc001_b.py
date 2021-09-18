import math


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    k = sum(B) - sum(A)
    if k < 0:
        print("No")
        return

    cnt = 0

    for i in range(n):
        # Aのみに注目して行えばいい
        cnt += max(0, (B[i] - A[i] + 1) // 2)
        if cnt > k:
            print("No")
            return

    print("Yes")


if __name__ == '__main__':
    main()
