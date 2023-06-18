import collections


def str2intWithArray(Array):  # 文字の配列を数字の配列に変換する
    return list(map(lambda x: int(x), Array))


def int2strWithArray(Array):  # 数字の配列を文字の配列に変換する
    return list(map(lambda x: str(x), Array))


def main():
    n = int(input())
    S = str2intWithArray(list(input()))
    if S.count(0) == 1:
        print(-1)
        return
    T = [S[i] * (i + 1) for i in range(n)]
    if S.count(0) == 0:
        print(' '.join(int2strWithArray(T)))
        return
    U = collections.deque()
    # まだ入ってない数字作成
    for p in range(n):
        if S[p] == 0:
            U.append(p + 1)
    u = U.popleft()
    U.append(u)

    for a in range(n):
        if T[a] == 0:
            w = U.popleft()
            T[a] = w

    print(' '.join(int2strWithArray(T)))


if __name__ == '__main__':
    main()
