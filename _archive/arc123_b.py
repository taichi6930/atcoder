
def main():
    n = int(input())
    [A, B, C] = [sorted(list(map(int, input().split()))) for _ in range(3)]

    ans = 0

    acnt, bcnt, ccnt = 0, 0, 0
    for i in range(10 ** 7):
        if acnt >= n or bcnt >= n or ccnt >= n:
            break

        if A[acnt] >= B[bcnt]:
            bcnt += 1
            continue

        if B[bcnt] >= C[ccnt]:
            ccnt += 1
            continue

        ans += 1
        acnt += 1
        bcnt += 1
        ccnt += 1

    print(ans)


if __name__ == '__main__':
    main()
