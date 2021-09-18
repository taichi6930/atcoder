def int2strWithArray(Array):  # 数字の配列を文字の配列に変換する
    return list(map(lambda x: str(x), Array))


def main():
    n = int(input())
    A = list(map(int, input().split()))
    ANS = [None for _ in range(n)]

    for k in range(n):
        x = k
        for i in range(n):
            if k + 1 == A[x]:
                ANS[k] = i + 1
                break
            x = A[x] - 1
    print(' '.join(int2strWithArray(ANS)))


if __name__ == '__main__':
    main()
