def main():
    n, t = map(int, input().split())
    A, B, AB = [None] * n, [None] * n, [None] * n
    for i in range(n):
        A[i], B[i] = map(int, input().split())
        AB[i] = A[i] - B[i]

    if sum(A) - t < 0:
        print(0)
        return

    if sum(B) - t > 0:
        print(-1)
        return

    AB.sort(reverse=True)

    cnt = 0
    for i in range(n):
        cnt += AB[i]
        if cnt >= sum(A) - t:
            print(i + 1)
            return


if __name__ == '__main__':
    main()
