def int2strWithArray(Array):  # 数字の配列を文字の配列に変換する
    return list(map(lambda x: str(x), Array))


def main():
    n = int(input())
    P = list(map(int, input().split()))
    Q = [None for _ in range(n)]

    for i in range(n):
        p = P[i]
        Q[p - 1] = i + 1
    print(' '.join(int2strWithArray(Q)))


if __name__ == '__main__':
    main()
