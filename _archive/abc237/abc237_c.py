from collections import Counter


def main():
    S = list(input())
    cS = Counter(S)
    print(cS)

    if len(S) == cS['a']:
        print('Yes')
        return
    cnt1 = 0
    for i in range(len(S)):
        if S[-1] != 'a':
            break
        S.pop()
        cnt1 += 1
    T = list(reversed(S))
    cnt2 = 0
    for i in range(len(T)):
        if T[-1] != 'a':
            break
        T.pop()
        cnt2 += 1
    print(cnt1, cnt2)
    print('Yes' if S == T else 'No')


if __name__ == '__main__':
    main()
