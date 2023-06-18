def int2strWithArray(Array):  # 数字の配列を文字の配列に変換する
    return list(map(lambda x: str(x), Array))


def main():
    n = int(input())
    A = list(map(int, input().split()))

    ansNum = A[0]
    k = 0

    for i in range(n):
        if ansNum == A[i]:
            continue
        k = ansNum
        if k <= ansNum and A[i] < ansNum:
            break

        ansNum = max(A[i], ansNum)

    ANS = []

    for j in range(n):
        if A[j] == ansNum:
            continue
        ANS.append(A[j])

    print(' '.join(int2strWithArray(ANS)))


if __name__ == '__main__':
    main()
