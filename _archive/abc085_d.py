import math


def main():
    n, h = map(int, input().split())
    A = [None] * n
    B = [None] * n
    for i in range(n):
        A[i], B[i] = map(int, input().split())
    A.sort(reverse=True)
    B.sort(reverse=True)

    cnt = 0
    for i in range(n):
        if B[i] <= A[0]:
            break
        cnt += 1
        h -= B[i]
        if h <= 0:
            break
    if h > 0:
        cnt += math.ceil(h / A[0])
    print(cnt)


if __name__ == '__main__':
    main()
